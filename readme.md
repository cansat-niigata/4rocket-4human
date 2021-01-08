
 ~~だいぶスパゲッティ~~

## windowsでの利用手順

### MSYS2のインストール

* まずMSYS2をインストールする( https://www.msys2.org )

### いろいろインストール

* したらMSYS2 MinGW-64bitでターミナルをひらいて

※32bitの場合は32bit版にすること

* 次に、gccとmakeをインストール

`$pacman -Sy`

`$pacman -Su`

`$pacman -S mingw-w64-x86_64-gcc`

`$pacman -S make`

### ForRocketをダウンロード

* ForRocketを git(https://github.com/sus304/ForRocket) から落としてForRocketディレクトリに移動

### そのままでもコンパイルできるけど単体で完結したバイナリがほしい！

* 適当なテキストエディタでmakefileを開く

* makefileのコンパイラオプションの項目を編集してMSYSから呼び出されるdllファイルを3つ静的リンク

```
## Compiler Option

####################################

CXXFLAGS=-Wall -std=gnu++11 -static -lstdc++ -lgcc -lwinpthread

RELEASE_FLAGS=-O2

TEST_FLAGS=-O0 -g -DDEBUG
```
    
### コンパイル！

* そしたらターミナルに戻って

`$make release`

* binディレクトリにForRocket.exeができるので好きなところに移動してpowershellかコマンドプロンプトでつかう

* ~~えくすかりば~~フロントエンドと同じディレクトリに置いてくれたらそれからも使える...と思う 
* Pythonで開く　から起動するとForRocketにアクセスできないっぽい→コマンドプロンプトかPowerShellから起動してほしい
~~結局コマンドラインから起動するんじゃ意味なくない？~~

### 本当はまずいかもしれないけど
* ソースコードをいじる
/src/factory/rocket_factory.cppの117行目を
```
rocket.setCdSParachute(jc.getSubItem("Constant CdS Parachute").getDouble("Constant CdS [-]"));
```
にするとcdsの値が後から設定できるかもしれない？

/src/solver/rocket_stage.cppの中の
```
fdr.dump_csvをfdr.DumpCsv
```
に置換するとmakeのときにエラーがでなくなるっぽい?

