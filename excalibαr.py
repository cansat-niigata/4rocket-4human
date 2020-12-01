import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os,sys
import subprocess
import json

class MakeSomething(tkinter.Frame):

    def __init__(self,master=None,geometry=None,title=None):
        super().__init__(master)
        #self.pack()

        master.geometry(geometry)
        master.title(title)

    def makeFrame(self,row,column=0,padding=10,sticky=tkinter.EW):
        frame = ttk.Frame(self.master,padding=padding)
        frame.grid(row=row,column=column,sticky=sticky)
        return frame

    def destroyFrame(self,frame):
        frame.pack_forget()

    def makeNumberBox(self,frame,entry,label=None,from_=0,to=10000,increment=1,format=None):
        labeltext = tkinter.Label(frame,text=label)
        labeltext.pack(side=tkinter.LEFT)
        spinbox = tkinter.Spinbox(frame,textvariable=entry,from_=from_,to=to,increment=increment,format=format)
        spinbox.pack(side=tkinter.LEFT)

    def makeTextBox(self,frame,entry,label=None,width=20):
        labeltext = tkinter.Label(frame,text=label)
        labeltext.pack(side=tkinter.LEFT)
        textbox = ttk.Entry(frame,textvariable=entry,width=width)
        textbox.pack(side=tkinter.LEFT)

    def makeFiledialogBox(self,frame,entry,label=None,ftyp=[('','*')]):
        ifilelabel = ttk.Label(frame,text=label,padding=(5,2))
        ifilelabel.pack(side=tkinter.LEFT)
        ifileentry = ttk.Entry(frame,textvariable=entry,width=30)
        ifileentry.pack(side=tkinter.LEFT)
        ifilebutton = ttk.Button(frame,text='参照',command=lambda:self.filedialog_clicked(entry,ftyp))
        ifilebutton.pack(side=tkinter.LEFT)

    """def makeSomeFiledialogBox(self,frame,entry=[],num=2,label=None,ftyp=[('','*')]):
        for i in range(num):
            entry0 = tkinter.StringVar()
            ifilelabel = ttk.Label(frame,text=label,padding=(5,2))
            ifilelabel.pack(side=tkinter.LEFT)
            ifileentry = ttk.Entry(frame,textvariable=entry0,width=30)
            ifileentry.pack(side=tkinter.LEFT)
            ifilebutton = ttk.Button(frame,text='参照',command=lambda:self.filedialog_clicked(entry0,ftyp))
            ifilebutton.pack(side=tkinter.LEFT)
            entry.append(entry0)"""

    """def makeFiledialog_clicked(self,framenum_init,entry=[],label=None,ftyp=[('','*')]):
        frame = self.makeFrame(row=framenum_init)
        entry0 = tkinter.StringVar()
        self.makeFiledialogBox(frame,entry0,label,ftyp)
        entry.append(entry0)
        plsbutton = ttk.Button(frame,text='+',command=lambda:[self.makeFiledialog_clicked(framenum_init+1,entry,label,ftyp),plsbutton.destroy()])
        plsbutton.pack(side=tkinter.LEFT)
        delbutton = ttk.Button(frame,text='-',command=frame.destroy)
        delbutton.pack(side=tkinter.LEFT)"""

    def filedialog_clicked(self,entry,ftyp):
        ifile = os.path.abspath(os.path.dirname(__file__))
        ifilepath = filedialog.askopenfilename(filetype = ftyp,initialdir = ifile)
        entry.set(ifilepath)    

    def makeButton(self,frame,label=None,command=None):
        button = ttk.Button(frame,text=label,command=command)
        button.pack(side=tkinter.LEFT)

    def makeCheckButton(self,frame,entry,label=None,onvalue=True,offvalue=False,command=None,trigger=True):
        if command != None:
            self.makeText(frame,label)
            rb = ttk.Checkbutton(frame,onvalue=onvalue,offvalue=offvalue,variable=entry,command=lambda:self.defineCheckbuttonCommand(var=entry,trigger=trigger,command=command))
            rb.pack(side=tkinter.LEFT)
        else:
            self.makeText(frame,label=label)
            rb = ttk.Checkbutton(frame,onvalue=onvalue,offvalue=offvalue,variable=entry)
            rb.pack(side=tkinter.LEFT)
        #entry.set(default)

    def defineCheckbuttonCommand(self,var,trigger,command):
        if var.get() == True:
            return command
        else:
            return None

    def makeText(self,frame,label):
        labeltext = tkinter.Label(frame,text=label)
        labeltext.pack(side=tkinter.LEFT)

class MakeSomething2:
    def __init__(self,master=None,width=1000,height=600,title=None,scroll_width=2000,scroll_height=2000,bg=None):
        master.geometry(str(width)+'x'+str(height))
       # master.geometry('1000x600')
        master.title(title)
        self.canvas = tkinter.Canvas(master,bg=bg)
        self.canvas.place(x=0,y=0,width=width,height=height)
        ybar = tkinter.Scrollbar(self.canvas,orient=tkinter.VERTICAL)
        xbar = tkinter.Scrollbar(self.canvas,orient=tkinter.HORIZONTAL)
        ybar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        xbar.pack(side=tkinter.BOTTOM,fill=tkinter.X)
        ybar.config(command=self.canvas.yview)
        xbar.config(command=self.canvas.xview)
        self.canvas.config(yscrollcommand=ybar.set,xscrollcommand=xbar.set)
        self.canvas.config(scrollregion=(0,0,scroll_width,scroll_height))
        self.mainframe = ttk.Frame(self.canvas)
        self.canvas.create_window((0,0),window=self.mainframe,anchor=tkinter.NW)       

    def makeFrame(self,row,column=0,padding=10,sticky=tkinter.EW):
        frame = ttk.Frame(self.mainframe,padding=padding)
        frame.grid(row=row,column=column,sticky=sticky)
        return frame

    def destroyFrame(self,frame):
        frame.pack_forget()

    def makeNumberBox(self,frame,entry,label=None,from_=0,to=10000,increment=1,format=None):
        labeltext = tkinter.Label(frame,text=label)
        labeltext.pack(side=tkinter.LEFT)
        spinbox = tkinter.Spinbox(frame,textvariable=entry,from_=from_,to=to,increment=increment,format=format)
        spinbox.pack(side=tkinter.LEFT)

    def makeTextBox(self,frame,entry,label=None,width=20):
        labeltext = tkinter.Label(frame,text=label)
        labeltext.pack(side=tkinter.LEFT)
        textbox = ttk.Entry(frame,textvariable=entry,width=width)
        textbox.pack(side=tkinter.LEFT)

    def makeFiledialogBox(self,frame,entry,label=None,ftyp=[('','*')]):
        ifilelabel = ttk.Label(frame,text=label,padding=(5,2))
        ifilelabel.pack(side=tkinter.LEFT)
        ifileentry = ttk.Entry(frame,textvariable=entry,width=30)
        ifileentry.pack(side=tkinter.LEFT)
        ifilebutton = ttk.Button(frame,text='参照',command=lambda:self.filedialog_clicked(entry,ftyp))
        ifilebutton.pack(side=tkinter.LEFT)

    def filedialog_clicked(self,entry,ftyp):
        ifile = os.path.abspath(os.path.dirname(__file__))
        ifilepath = filedialog.askopenfilename(filetype = ftyp,initialdir = ifile)
        entry.set(ifilepath)    

    def makeButton(self,frame,label=None,command=None):
        button = ttk.Button(frame,text=label,command=command)
        button.pack(side=tkinter.LEFT)

    def makeCheckButton(self,frame,entry,label=None,onvalue=True,offvalue=False,command=None,trigger=True):
        if command != None:
            self.makeText(frame,label)
            rb = ttk.Checkbutton(frame,onvalue=onvalue,offvalue=offvalue,variable=entry,command=lambda:self.defineCheckbuttonCommand(var=entry,trigger=trigger,command=command))
            rb.pack(side=tkinter.LEFT)
        else:
            self.makeText(frame,label=label)
            rb = ttk.Checkbutton(frame,onvalue=onvalue,offvalue=offvalue,variable=entry)
            rb.pack(side=tkinter.LEFT)
        #entry.set(default)

    def defineCheckbuttonCommand(self,var,trigger,command):
        if var.get() == True:
            return command
        else:
            return None

    def makeText(self,frame,label):
        labeltext = tkinter.Label(frame,text=label)
        labeltext.pack(side=tkinter.LEFT)



def terminate(root):
        if messagebox.askokcancel("quit",'do you want to quit?'):
            root.destroy()

def executeForRocket(solverconfigpath):
    path =  solverconfigpath.get()
    
    subprocess.run(os.path.abspath(os.path.dirname(__file__))+'\\ForRocket.exe -v')
    subprocess.run(os.path.abspath(os.path.dirname(__file__))+'\\ForRocket.exe '+path)
    print('\n')
    #tkinter.messagebox.showinfo(title='warning!',message='工事中につき機能しません')

def makeNewSolverConfig_clicked(configpath):
    root1 = tkinter.Toplevel()
    root1.protocol("WM_DELETE_WINDOW",lambda:terminate(root1))
    window1 = MakeSomething(master=root1,title='ForRocket for Human@newconfig')

    frame1 = window1.makeFrame(row=0)
    model_name = tkinter.StringVar()
    window1.makeTextBox(frame1,model_name,label='Model_Name')
    launch_date = tkinter.StringVar()
    window1.makeTextBox(frame1,launch_date,label='Launch DateTime[YYYY/MM/DD h:mm:ss.s]>>')

    frame3 = window1.makeFrame(row=1)
    window1.makeText(frame3,label='Launch Condition')

    frame4 = window1.makeFrame(row=2)
    latitude = tkinter.StringVar()
    longitude = tkinter.StringVar()
    height_for_WGS84 = tkinter.StringVar()
    window1.makeNumberBox(frame4,latitude,label='Latitude[deg]>>',from_=-180,to=180,increment=0.0000001)
    window1.makeNumberBox(frame4,longitude,label='Longitude[deg]>>',from_=-90,to=90,increment=0.0000001)
    window1.makeNumberBox(frame4,height_for_WGS84,label='Height for WGS84[deg]>>',from_=-180,to=180)
    latitude.set(0)
    longitude.set(0)
    height_for_WGS84.set(0)

    frame5 = window1.makeFrame(row=3)
    azimuth = tkinter.StringVar()
    elevation = tkinter.StringVar()
    window1.makeNumberBox(frame5,azimuth,label='Azimuth[deg]>>',from_=0,to=360,increment=0.1)
    window1.makeNumberBox(frame5,elevation,label='Elevation[deg]>>',from_=-180,to=180,increment=0.1)
    azimuth.set(0)
    elevation.set(0)

    frame6 = window1.makeFrame(row=4)
    north_velocity = tkinter.StringVar()
    east_velocity = tkinter.StringVar()
    down_velocity = tkinter.StringVar()
    window1.makeNumberBox(frame6,north_velocity,label='North Velocity[m/s]>>',from_=-1000)
    window1.makeNumberBox(frame6,east_velocity,label='East Velocity[m/s]>>',from_=-1000)
    window1.makeNumberBox(frame6,down_velocity,label='Down Velocity[m/s]>>',from_=-1000)
    north_velocity.set(0)
    east_velocity.set(0)
    down_velocity.set(0)

    frame7 = window1.makeFrame(row=5)
    windfilepath = tkinter.StringVar()
    window1.makeFiledialogBox(frame7,windfilepath,label='Wind_Data_File>>',ftyp=[('csvファイル','.csv')])
    bvar = tkinter.BooleanVar()
    #window1.makeCheckButton(frame7,label='disable wind file&Use constant Wind Data[m/s]>>',entry=bvar,onvalue=False,offvalue=True)
    window1.makeCheckButton(frame7,label='disable wind file>>',entry=bvar,onvalue=False,offvalue=True)
    bvar.set(True)


    #constant_wind = tkinter.StringVar()
    #window1.makeNumberBox(frame7,entry=constant_wind)

    """stage_config_paths = []
    frame8 = window1.makeFrame(8)
    entry0 = tkinter.StringVar()
    window1.makeFiledialogBox(frame8,entry0,label='stage_config_json>>',ftyp=[('jsonファイル','.json')])
    stage_config_paths.append(entry0)
    plsbutton = ttk.Button(frame8,text='+',command=lambda:[window1.makeFiledialog_clicked(10,stage_config_paths,label='stage_config_json>>',ftyp=[('jsonファイル','.json')])])
    plsbutton.pack(side=tkinter.LEFT)"""

    frame8 = window1.makeFrame(8)
    frame9 = window1.makeFrame(9)
    frame10 = window1.makeFrame(10)
    frame11 = window1.makeFrame(11)
    number_stage = tkinter.StringVar()
    stage_config_path_1st = tkinter.StringVar()
    stage_config_path_2nd = tkinter.StringVar()
    stage_config_path_3rd = tkinter.StringVar()
    window1.makeNumberBox(frame8,number_stage,label='Number of Stages>>',from_=1,to=3)
    window1.makeFiledialogBox(frame9,entry=stage_config_path_1st,label='1st Stage Config>>',ftyp=[('jsonファイル','.json')])
    window1.makeFiledialogBox(frame10,entry=stage_config_path_2nd,label='2nd Stage Config>>',ftyp=[('jsonファイル','.json')])
    window1.makeFiledialogBox(frame11,entry=stage_config_path_3rd,label='3rd Stage Config>>',ftyp=[('jsonファイル','.json')])
    button1 = ttk.Button(frame9,text='新規ファイルを作成する(config.json)',command=lambda:makeNewStageConfig_clicked(stage_config_path_1st))
    button2 = ttk.Button(frame10,text='新規ファイルを作成する(config.json)',command=lambda:makeNewStageConfig_clicked(stage_config_path_2nd))
    #button3 = ttk.Button(frame11,text='make new stage3 config')
    window1.makeButton(frame11,label='新規ファイルを作成する(config.json)',command=lambda:makeNewStageConfig_clicked(stage_config_path_3rd))
    button1.pack(side=tkinter.LEFT)
    button2.pack(side=tkinter.LEFT)
    #button3.pack(side=tkinter.LEFT)

        
    frame12 = window1.makeFrame(12)

    execbutton = ttk.Button(frame12,text='Execute JSONdump',command=lambda:[makeSolverConfigJson_clicked(configpath,model_name.get(),launch_date.get(),latitude.get(),longitude.get(),height_for_WGS84.get(),azimuth.get(),elevation.get(),north_velocity.get(),east_velocity.get(),down_velocity.get(),bvar.get(),windfilepath.get(),number_stage.get(),stage_config_path_1st.get(),stage_config_path_2nd.get(),stage_config_path_3rd.get())])
    execbutton.pack(side=tkinter.LEFT)

    root1.mainloop()

def makeSolverConfigJson_clicked(entry,model_name,launch_date,latitude,longitude,height_for_WGS84,azimuth,elevation,north_velocity,east_velocity,down_velocity,windmode,windfilepath,number_stage,stage_config_path_1st,stage_config_path_2nd=None,stage_config_path_3rd=None):
    config_json_dict = {
        "Model ID":model_name,
        "Launch DateTime":launch_date,
        "Launch Condition":{
            "Latitude [deg]":float(latitude),
            "Longitude [deg]":float(longitude),
            "Height for WGS84 [deg]":float(height_for_WGS84),
            "Azimuth [deg]":float(azimuth),
            "Elevation [deg]":float(elevation),
            "North Velocity [m/s]":float(north_velocity),
            "East Velocity [m/s]":float(east_velocity),
            "Down Velocity [m/s]":float(down_velocity),
        },
        "Wind Condition":{
            "Enable Wind":windmode,
            "Wind File Path":windfilepath
        },
        "Number of Stage":int(number_stage),
        "Stage1 Config File List": stage_config_path_1st,
	    "Stage2 Config File List": stage_config_path_2nd,
	    "Stage3 Config File List": stage_config_path_3rd
    }
    
    with open ((os.path.abspath(os.path.dirname(__file__))+'\\'+model_name+'_config.json'),'w') as f:
        json.dump(config_json_dict, f, indent=4, ensure_ascii=False)

    entry.set((os.path.abspath(os.path.dirname(__file__))+'\\'+model_name+'_config.json'))
    print(os.path.abspath(os.path.dirname(__file__))+'\\'+model_name+'_config.json is dumped')

def makeNewStageConfig_clicked(configpath):
    root2 = tkinter.Toplevel()
    root2.protocol("WM_DELETE_WINDOW",lambda:terminate(root2))
    window2 = MakeSomething(master=root2,title='ForRocket for Human@new stageconfig')
    
    frame0 = window2.makeFrame(1)
    stage_name = tkinter.StringVar()
    window2.makeTextBox(frame0,stage_name,'filename>>')

    frame1 = window2.makeFrame(2)
    frame2 = window2.makeFrame(3)
    frame3 = window2.makeFrame(4)

    rocket_configuration_file_path = tkinter.StringVar()
    engine_configuration_file_path = tkinter.StringVar()
    sequence_configuration_file_path = tkinter.StringVar()
    window2.makeFiledialogBox(frame1,rocket_configuration_file_path,'Rocket Configuration File Path>>',[('jsonファイル','.json')])
    window2.makeButton(frame1,'新規ファイルを作成する(config.json)',command=lambda:makeNewRocketConfig_clicked(rocket_configuration_file_path))
    window2.makeFiledialogBox(frame2,engine_configuration_file_path,'Engine Configuration File Path>>',[('jsonファイル','.json')])
    window2.makeButton(frame2,'新規ファイルを作成する(config.json)',command=lambda:makeNewEngineConfig_clicked(rocket_configuration_file_path))
    window2.makeFiledialogBox(frame3,sequence_configuration_file_path,'Sequence Configuration File Path>>',[('jsonファイル','.json')])
    window2.makeButton(frame3,'新規ファイルを作成する(config.json)',command=lambda:makeNewEngineConfig_clicked(sequence_configuration_file_path))

    frame5 = window2.makeFrame(5)
    window2.makeButton(frame5,'Execute JSONdump',command=lambda:makeNewStageConfigJson_clicked(configpath,stage_name.get(),rocket_configuration_file_path.get(),engine_configuration_file_path.get(),sequence_configuration_file_path.get()))

    root2.mainloop()

def makeNewStageConfigJson_clicked(entry,name,rocket_configuration_file_path,engine_configuration_file_path,sequence_configuration_file_path):
    config_json_dict = {
        "Rocket Configuration File Path":rocket_configuration_file_path,
        "Engine Configuration File Path":engine_configuration_file_path,
        "Sequence of Event File Path":sequence_configuration_file_path
    }
    
    with open ((os.path.abspath(os.path.dirname(__file__))+'\\'+name+'stage_config.json'),'w') as f:
        json.dump(config_json_dict, f, indent=4, ensure_ascii=False)

    entry.set((os.path.abspath(os.path.dirname(__file__))+'\\'+name+'stage_config.json'))
    print(os.path.abspath(os.path.dirname(__file__))+'\\'+name+'_config.json is dumped')

def makeNewRocketConfig_clicked(configpath):
    root3 = tkinter.Toplevel()
    root3.protocol("WM_DELETE_WINDOW",lambda:terminate(root3))
    window3 = MakeSomething2(master=root3,width=1100,height=600,title='ForRocket for Human@new rocketconfig',scroll_height=1200)

    name = tkinter.StringVar()
    frame0 = window3.makeFrame(0)
    window3.makeTextBox(frame0,name,'filename>>')

    diameter = tkinter.StringVar()
    length = tkinter.StringVar()
    frame1 = window3.makeFrame(1)
    window3.makeNumberBox(frame1,diameter,'Diameter[mm]>>',increment=0.1)
    window3.makeNumberBox(frame1,length,'Length[mm]>>',increment=0.1)
    
    frame2 = window3.makeFrame(2)
    window3.makeText(frame2,'Mass')

    inert =tkinter.StringVar()
    propellant = tkinter.StringVar()
    frame3 = window3.makeFrame(3)
    window3.makeNumberBox(frame3,inert,'Inert[kg]>>',increment=0.001)
    window3.makeNumberBox(frame3,propellant,'Propellant[kg]>>',increment=0.001)

    frame4 = window3.makeFrame(4)
    enable_program_attitude = tkinter.BooleanVar()
    program_attitude_filepath = tkinter.StringVar()
    window3.makeText(frame4,label='Enable Program Attitude>>')
    rb = ttk.Checkbutton(frame4,onvalue=True,offvalue=False,variable=enable_program_attitude,command=lambda:enableprogramattitude_message(enable_program_attitude))
    rb.pack(side=tkinter.LEFT)
    window3.makeFiledialogBox(frame4,program_attitude_filepath,'Program Attitude File Path>>',[('csvファイル','.csv')])

    frame5 = window3.makeFrame(5)
    frame6 = window3.makeFrame(6)
    constant_xcg = tkinter.StringVar()
    enable_xcg = tkinter.BooleanVar()
    xcg_filepath = tkinter.StringVar()
    window3.makeText(frame5,'Center of Gravity(X axis?)')
    window3.makeNumberBox(frame6,constant_xcg,'Constant X-C.G. from BodyTail[mm]>>',increment=0.1)
    window3.makeCheckButton(frame6,enable_xcg,'Enable X-C.G.>>')
    window3.makeFiledialogBox(frame6,xcg_filepath,'X-C.G File Path>>',[('csvファイル','.csv')])

    frame7 = window3.makeFrame(7)
    frame8 = window3.makeFrame(8)
    frame9 = window3.makeFrame(9)
    constant_mi_yaw = tkinter.StringVar()
    constant_mi_picth = tkinter.StringVar()
    constant_mi_roll = tkinter.StringVar()
    enable_mi = tkinter.BooleanVar()
    mi_filepath = tkinter.StringVar()
    window3.makeText(frame7,'Morment of Inertia')
    window3.makeNumberBox(frame8,constant_mi_yaw,'Constant M.I. Yaw Axis[kg-m2]>>',increment=0.001)
    window3.makeNumberBox(frame8,constant_mi_picth,'Constant M.I. Pitch Axis[kg-m2]>>',increment=0.001)
    window3.makeNumberBox(frame8,constant_mi_roll,'Constant M.I. Roll[kg-m2]>>',increment=0.001)
    window3.makeCheckButton(frame9,enable_mi,'Enable M.I. File>>')
    window3.makeFiledialogBox(frame9,mi_filepath,'M.I. File Path>>',[('csvファイル','.csv')])

    frame10 = window3.makeFrame(10)
    frame11 = window3.makeFrame(11)
    constant_xcp = tkinter.StringVar()
    enable_xcp = tkinter.BooleanVar()
    xcp_filepath = tkinter.StringVar()
    window3.makeText(frame10,'Center of Pressure(X axis?)')
    window3.makeNumberBox(frame11,constant_xcp,'Constant X-C.P. from BodyTail[mm]>>',increment=0.1)
    window3.makeCheckButton(frame11,enable_xcp,'Enable X-C.P.>>')
    window3.makeFiledialogBox(frame11,xcp_filepath,'X-C.P File Path>>',[('csvファイル','.csv')])

    frame12 = window3.makeFrame(12)
    x_thrustloadingpoint = tkinter.StringVar()
    window3.makeNumberBox(frame12,x_thrustloadingpoint,'X-ThrustLoadingPoint from BodyTail[mm]>>',increment=0.1)

    frame13 = window3.makeFrame(13)
    frame14 = window3.makeFrame(14)
    frame15 = window3.makeFrame(15)
    constant_ca = tkinter.StringVar()
    constant_ca_burnout = tkinter.StringVar()
    enable_ca = tkinter.BooleanVar()
    ca_filepath = tkinter.StringVar()
    enable_ca_burnout = tkinter.BooleanVar()
    ca_burnout_filepath = tkinter.StringVar() 
    window3.makeText(frame13,'Axial Force Coefficient')
    window3.makeNumberBox(frame14,constant_ca,'Constant CA[-]>>',increment=0.1)
    window3.makeNumberBox(frame14,constant_ca_burnout,'Constant BurnOut CA[-]>>',increment=0.1)
    window3.makeCheckButton(frame15,enable_ca,'Enable CA File>>')
    window3.makeFiledialogBox(frame15,ca_filepath,'CA File Path>>',[('csvファイル','.csv')])
    window3.makeCheckButton(frame15,enable_ca_burnout,'Enable CA(BurnOut) File>>')
    window3.makeFiledialogBox(frame15,ca_burnout_filepath,'CA(BurnOut) File Path>>',[('csvファイル','.csv')])

    frame16 = window3.makeFrame(16)
    frame17 = window3.makeFrame(17)
    constant_cna = tkinter.StringVar()
    enable_cna = tkinter.BooleanVar()
    cna_filepath = tkinter.StringVar()
    window3.makeText(frame16,'Normal Force div AoA Coefficient')
    window3.makeNumberBox(frame17,constant_cna,'Constant CNa[1/rad]>>',increment=0.1)
    window3.makeCheckButton(frame17,enable_cna,'Enable CNa File>>')
    window3.makeFiledialogBox(frame17,cna_filepath,'CNa File Path>>',[('csvファイル','.csv')])
    
    frame18 = window3.makeFrame(18)
    frame19 = window3.makeFrame(19)
    frame20 = window3.makeFrame(20)
    fin_cant_angle = tkinter.StringVar()
    enable_cld = tkinter.BooleanVar()
    constant_cld = tkinter.StringVar()
    cld_filepath = tkinter.StringVar()
    window3.makeText(frame18,'Roll Force div FinCantAngle Coefficient')
    window3.makeNumberBox(frame19,fin_cant_angle,'Fin Cant Angle[deg]>>',increment=0.1)
    window3.makeNumberBox(frame19,constant_cld,'Constant Cld[1/rad]>>',increment=0.1)
    window3.makeCheckButton(frame20,enable_cld,'Enable Cld File>>')
    window3.makeFiledialogBox(frame20,cld_filepath,'Cld File Path>>',[('csvファイル','.csv')])

    frame21 = window3.makeFrame(21)
    frame22 = window3.makeFrame(22)
    constant_clp = tkinter.StringVar()
    enable_clp = tkinter.BooleanVar()
    clp_filepath = tkinter.StringVar()
    window3.makeText(frame21,'Roll Damping Moment Coefficient')
    window3.makeNumberBox(frame22,constant_clp,'Constant Clp[-]>>',increment=0.1)
    window3.makeCheckButton(frame22,enable_clp,'Enable Clp File>>')
    window3.makeFiledialogBox(frame22,clp_filepath,'Clp File Path>>',[('csvファイル','.csv')])

    frame23 = window3.makeFrame(23)
    frame24 = window3.makeFrame(24)
    constant_cmq = tkinter.StringVar()
    enable_cmq = tkinter.BooleanVar()
    cmq_filepath = tkinter.StringVar()
    window3.makeText(frame23,'Pitch Damping Moment Coefficient')
    window3.makeNumberBox(frame24,constant_cmq,'Constant Cmq[-]>>',increment=0.1)
    window3.makeCheckButton(frame24,enable_cmq,'Enable Cmq File>>')
    window3.makeFiledialogBox(frame24,cmq_filepath,'Cmq File Path>>',[('csvファイル','.csv')])

    frame25 = window3.makeFrame(25)
    frame26 = window3.makeFrame(26)
    constant_cnr = tkinter.StringVar()
    enable_cnr = tkinter.BooleanVar()
    cnr_filepath = tkinter.StringVar()
    window3.makeText(frame25,'Yaw Damping Moment Coefficient')
    window3.makeNumberBox(frame26,constant_cnr,'Constant Cnr[-]>>',increment=0.1)
    window3.makeCheckButton(frame26,enable_cnr,'Enable Cnr File>>')
    window3.makeFiledialogBox(frame26,cnr_filepath,'Cnr File Path>>',[('csvファイル','.csv')])

    frame27 = window3.makeFrame(27)
    window3.makeButton(frame27,'Execute JSONdump',command=lambda:makeNewRocketConfigJson_clicked(configpath,name.get(),diameter.get(),length.get(),inert.get(),propellant.get(),enable_program_attitude.get(),program_attitude_filepath.get(),enable_xcg.get(),constant_xcg.get(),xcg_filepath.get(),enable_mi.get(),constant_mi_yaw.get(),constant_mi_picth.get(),constant_mi_roll.get(),mi_filepath.get(),enable_xcp.get(),constant_xcp.get(),xcp_filepath.get(),enable_ca.get(),constant_ca.get(),ca_filepath.get(),enable_ca_burnout.get(),constant_ca_burnout.get(),ca_burnout_filepath.get(),enable_cna.get(),constant_cna.get(),cna_filepath.get(),enable_cld.get(),fin_cant_angle.get(),constant_cld.get(),cld_filepath.get(),enable_clp.get(),constant_clp.get(),clp_filepath.get(),enable_cmq.get(),constant_cmq.get(),cmq_filepath.get(),enable_cnr.get(),constant_cnr.get(),cnr_filepath.get()))

    root3.mainloop()

def enableprogramattitude_message(var):
    if var.get() == True:
        tkinter.messagebox.showinfo('caution!',message='姿勢制御はsequence_of_event.jsonでも有効である必要があります')

def makeNewRocketConfigJson_clicked(entry,name,diameter,length,inert,propellant,enable_program_attitude,program_attitude_filepath,enable_xcg,constant_xcg,xcg_filepath,enable_mi,constant_mi_yaw,constant_mi_picth,constant_mi_roll,mi_filepath,enable_xcp,constant_xcp,xcp_filepath,enable_ca,constant_ca,ca_filepath,enable_ca_burnout,constant_ca_burnout,ca_burnout_filepath,enable_cna,constant_cna,cna_filepath,enable_cld,fin_cant_angle,constant_cld,cld_filepath,enable_clp,constant_clp,clp_filepath,enable_cmq,constant_cmq,cmq_filepath,enable_cnr,constant_cnr,cnr_filepath):
    config_json_dict = {
        "Diameter [mm]":float(diameter),
        "Length [mm]":float(length),
        "Mass":{
            "Inert[kg]":float(inert),
            "Propellant[kg]":float(propellant)
        },
        "Enable Program Attitude":enable_program_attitude,
        "Program Attitude File":{
            "Program Attitude File Path":program_attitude_filepath
        },
        "Enable X-C.G. File":enable_xcg,
        "X-C.G. File":{
            "X-C.G. File Path":xcg_filepath
        },
        "Constant X-C.G.":{
            "Constant X-C.G. fome BodyTail [mm]":float(constant_xcg)
        },
        "Comment M.I.":"Moment of Inertia",
        "Enable M.I. File":enable_mi,
        "M.I. File":{
            "M.I. File Path":mi_filepath
        },
        "Constant M.I.":{
            "Yaw Axis [kg-m2]":float(constant_mi_yaw),
            "Pitch Axis [kg-m2]":float(constant_mi_picth),
            "Roll Axis[kg-m2]":float(constant_mi_roll)
        },
        "Enable X-C.P. File":enable_xcp,
        "X-C.P. File":{
            "X-C.P.":xcp_filepath
        },
        "Constant X-C.P.":{
            "Constant X-C.P. from BodyTail [mm]":float(constant_xcp)
        },
        "Comment CA":"Axial Force Coefficient",
        "Enable CA File":enable_ca,
        "CA File":{
            "CA File Path":ca_filepath,
            "BurnOut CA File Path":ca_burnout_filepath
        },
        "Constant CA":{
            "Constant CA [-]":float(constant_ca),
            "Constant BurnOut CA [-]":float(constant_ca_burnout)
        },
        "Comment CNa":"Normal Force div AoA Coefficient",
        "Enable CNa File":enable_cna,
        "CNa File":{
            "CNa File Path":cna_filepath
        },
        "Constant CNa":{
            "Costant CNa [1/rad]":float(constant_cna)
        },
        "Comment Cld":"Roll Force div FinCantAngle Coefficient",
        "Fin Cant Angle [deg]":float(fin_cant_angle),
        "Enable Cld File":enable_cld,
        "Cld File":{
            "Cld File Path":cld_filepath
        },
        "Constant Cld":{
            "Constant Cld [1/rad]":float(constant_cld)
        },
        "Comment Clp":"Roll Damping Moment Coefficient",
        "Enable Clp File":enable_clp,
        "Clp File":{
            "Clp File Path":clp_filepath
        },
        "Constant Clp":{
            "Constant Clp [-]":float(constant_clp)
        },
        "Comment Cmq":"Pitch Damping Moment Coefficient",
        "Enable Cmq File":enable_cmq,
        "Cmq File":{
            "Cmq File Path":cmq_filepath,
        },
        "Constant Cmq":{
            "Constant Cmq [-]":constant_cmq
        },
        "Comment Cnr":"Yaw Damping Moment Coefficient",
        "Enable Cnr File":enable_cnr,
        "Cnr File":{
            "Cnr File Path":cnr_filepath
        },
        "Constant Cnr":{
            "Constant Cnr [-]":constant_cnr
        }
    }
    
    with open ((os.path.abspath(os.path.dirname(__file__))+'\\'+name+'rocket_config.json'),'w') as f:
        json.dump(config_json_dict, f, indent=4, ensure_ascii=False)

    entry.set((os.path.abspath(os.path.dirname(__file__))+'\\'+name+'rocket_config.json'))
    print(os.path.abspath(os.path.dirname(__file__))+'\\'+name+'_config.json is dumped')

def makeNewEngineConfig_clicked(configpath):
    tkinter.messagebox.showinfo(title='warning!',message='工事中につき機能しません')

def makeNewSequenceConfig_clicked(configpath):
    tkinter.messagebox.showinfo(title='warning!',message='工事中につき機能しません')

def main():
    print('excalibar_alpha v0.1.4')
    root0 = tkinter.Tk()
    root0.protocol("WM_DELETE_WINDOW",lambda:terminate(root0))
    window0 = MakeSomething(master=root0,title='ForRocket for Human@entry')

    frame0 = window0.makeFrame(0)
    window0.makeText(frame0,'これはForRocket用簡易GUI＆設定ファイル作成支援システムです')

    frame1 = window0.makeFrame(row=1,column=0)
    configfilepath = tkinter.StringVar()
    window0.makeFiledialogBox(frame1,configfilepath,label='config.json>>',ftyp=[('jsonファイル','.json')])

    frame2 = window0.makeFrame(row=2,column=0)
    button1 = ttk.Button(frame2,text='execute ForRocket',command=lambda:executeForRocket(configfilepath))
    button1.pack(side=tkinter.LEFT)
    button2 = ttk.Button(frame2,text='新規ファイルを作成する(config.json)',command=lambda:makeNewSolverConfig_clicked(configfilepath))
    button2.pack(side=tkinter.LEFT)

    window0.mainloop()

if __name__ == '__main__':
    main()



    


