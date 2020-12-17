import requests
import numpy
import folium
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
#from matplotlib._png import read_png
from matplotlib.cbook import get_sample_data
from io import BytesIO
from PIL import Image
import cv2
import csv
import argparse

def LatLng2Tile(latitude,longitude,zoomlevel=18):
	n = 2**zoomlevel
	x = int((longitude + 180)*n/360)
	y = int((1 - numpy.arcsinh(numpy.tan(numpy.deg2rad(latitude)))/numpy.pi)*n/2)
	return [y,x]

def LatLng2Pixel(latitude,longitude,zoomlevel):
	n = 2**zoomlevel
	x = int((longitude + 180)*n/360)
	y = int((1 - numpy.arcsinh(numpy.tan(numpy.deg2rad(latitude)))/numpy.pi)*n/2)
	return [y,x]

def getTilefromGSI(x,y,z=18,url_="https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png",filename=None):
	url = url_.format(z=str(z),x=str(x),y=str(y))
	print("\r[{}]".format('request:'+url, end=""))
	print("\r[{}]".format('fetching...'))
	res = requests.get(url)
	if res.status_code == 200:
		img = res.content
		print("\r[{}]".format('complete!'))
		if filename != None:
			with open(filename,'wb') as file:
				file.write(img)
		return {
			'img':numpy.asarray(Image.open(BytesIO(img)).convert('RGB')),
			'x':x,
			'y':y
		}
	else:
		raise Exception("{} returned {}".format(res.url, res.status_code))

def constructMap(top=101239,left=232243,bottom=101240,right=232244,zoomlevel=18,filename=None,url_=None):
	lengthX = right - left + 1
	lengthY = bottom - top + 1
	rows = []
	for y in range(lengthY):
		row = []
		for x in range(lengthX):
			try:
				if url_ != None:
					result = getTilefromGSI(left+x,top+y,zoomlevel,url_=url_)
				else:
					result = getTilefromGSI(left+x,top+y,zoomlevel)
				print("\r[{}]".format(('progress:	'+str(y*lengthX + x+1)+'/'+str(lengthX*lengthY)), end=""))
				#print('progress:	'+str(y*lengthX + x+1)+'/'+str(lengthX*lengthY))
			except Exception as e:
				raise e				
			row.append(result['img'])
		rows.append(row)
	map_ = cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in rows])

	if filename != None:
		cv2.imwrite(filename,map_)
	else:
		cv2.imshow('img',map_)
	
	return map_




def getLine_3D_prototype(csvfile,plot_option=False,createmap=False):#試作段階,取り敢えずForRocket用フォーマットで

	with open(csvfile,'r') as file:
		datas = csv.DictReader(file)
		latitude = []
		longitude = []
		altitude = []
		timestamp = []

		for row in datas:
			latitude.append(float(row['Latitude [deg]']))
			longitude.append(float(row['Longitude [deg]']))
			altitude.append(float(row['Altitude [m]']))
			timestamp.append(float(row['Time [s]']))

		if createmap == True:
			north = max(latitude)
			south = min(latitude)
			east = max(longitude)
			west = min(longitude)

			filename = './map.png'
			zoom = 13
			top,left = LatLng2Tile(north,west,zoom)
			bottom,right = LatLng2Tile(south,east,zoom)

			constructMap(top,left,bottom,right,zoom,filename)
			#img = plt.imread(filename)

		if plot_option == True:
			ax3D = plt.subplot2grid((3,6),(0,0),3,3,projection='3d')
			axlat = plt.subplot2grid((3,6),(0,4),colspan=2)
			axlng = plt.subplot2grid((3,6),(1,4),colspan=2)
			axalt = plt.subplot2grid((3,6),(2,4),colspan=2)

			#X1, Y1 = numpy.ogrid[0:img.shape[0], 0:img.shape[1]]
			#ax3D.plot_surface(X1, Y1, numpy.atleast_2d(0), rstride=5, cstride=5, facecolors=img)

			ax3D.plot(longitude,latitude,altitude)
			axlat.plot(timestamp,latitude)
			axlng.plot(timestamp,longitude)
			axalt.plot(timestamp,altitude)
		else:
			fig = plt.figure()
			ax3D = fig.add_subplot(111,projection='3d')
			ax3D.plot(longitude,latitude,altitude)
			
		ax3D.scatter(longitude[0],latitude[0],altitude[0],label='Start',color='red')
		leng = len(timestamp) - 1
		ax3D.scatter(longitude[leng],latitude[leng],altitude[leng],label='End',color='orange')

		ax3D.set_title('Route')
		ax3D.set_xlabel('Longitude[deg]')
		ax3D.set_ylabel('Latitude[deg]')
		ax3D.set_zlabel('Altitude[m]')

		plt.tight_layout()
		plt.legend()
		plt.show()

def getLine_2D_prototype(csvfile,imgfile=None):
	with open(csvfile,'r') as file:
		datas = csv.DictReader(file)
		latitude = []
		longitude = []
		#altitude = []
		timestamp = []

		for row in datas:
			latitude.append(float(row['Latitude [deg]']))
			longitude.append(float(row['Longitude [deg]']))
			#altitude.append(float(row['Altitude [m]']))
			timestamp.append(float(row['Time [s]']))

		if imgfile == None:
			north = max(latitude)
			south = min(latitude)
			east = max(longitude)
			west = min(longitude)
			print(north)
			print(west)
			print(south)
			print(east)

			filename = './map.png'
			zoom = 13
			top,left = LatLng2Tile(north,west,zoom)
			bottom,right = LatLng2Tile(south,east,zoom)

			constructMap(top,left,bottom,right,zoom,filename)

			"""for i in range(len(timestamp)):
				y,x = LatLng2Pixel(longitude[i],longitude[i],zoom)
				latitude[i] = y
				longitude[i] = x"""
		else:
			filename = imgfile

		fig = plt.figure()
		ax = fig.add_subplot(111)

		img = Image.open(filename)
		ax.imshow(img)

		ax.plot(longitude,latitude)
		ax.scatter(longitude[0],latitude[0],label='Start',color='red')
		leng = len(timestamp) - 1
		ax.scatter(longitude[leng],latitude[leng],label='End',color='orange')

		ax.set_title('Route')
		ax.set_xlabel('Longitude[deg]')
		ax.set_ylabel('Latitude[deg]')

		plt.show()

def getLine_2D_prototype_B(csvfile,outfile='map.html'):
	with open(csvfile,'r') as file:
		datas = csv.DictReader(file)
		latitude = []
		longitude = []
		#altitude = []
		timestamp = []

		for row in datas:
			latitude.append(float(row['Latitude [deg]']))
			longitude.append(float(row['Longitude [deg]']))
			#altitude.append(float(row['Altitude [m]']))
			timestamp.append(float(row['Time [s]']))


	lat_ave = 0
	lng_ave = 0
	num = len(timestamp)
	for i in range(num):
		lat_ave += latitude[i]
		lng_ave += longitude[i]
	lat_ave /= num
	lng_ave /= num

	mp = folium.Map(location=[lat_ave,lng_ave],zoom_start=18,max_zoom=20,max_native_zoom=18)

	folium.Marker(
		location=[latitude[0],longitude[0]],
		popup='START',
		icon=folium.Icon(color='red')
	).add_to(mp)

	folium.Marker(
		location=[latitude[num-1],longitude[num-1]],
		popup='END',
		icon=folium.Icon(color='blue')
	).add_to(mp)

	for i in range(num-1):
		folium.vector_layers.PolyLine(locations=[
			[latitude[i],longitude[i]],
			[latitude[i+1],longitude[i+1]]
		],
		color='orange',
		weight=1
		).add_to(mp)

	mp.save(outfile)
		

if __name__ == "__main__":
	"""parser = argparse.ArgumentParser(
		prog='nine_point_eight ver.β',
		usage='osmliner.py file.csv',
		description='...',
		#epilog='',
		add_help=True,
	)
	parser.add_argument('-m','--mark',help='mark waypoint',store_true=True)
	parser.add_argument('-d','--3d',help='3d graph mode',store_false=True)
	parser.add_argument('-t','--2d',help='2d graph mode')
	args = parser.parse_args()"""

	getLine_2D_prototype_B("./flight_log.csv")
	getLine_3D_prototype("./flight_log.csv")


	

	



