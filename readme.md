 ~~誰か開発引き継いでくれ~~
 ~~つか誰だよこんなスパゲッティ書いたやつ~~

## windowsでの利用手順

### MSYS2のインストール

* まずMSYS2をインストールする（https://www.msys2.org/）

### いろいろインストール

* したらMSYS2 MinGW-64bitでターミナルをひらいて

(32bitのひとは32bitにしようね。gccもね）

* 次に、gccとmakeをインストール

`$pacman -Sy`

`$pacman -Su`

`$pacman -S mingw-w64-x86_64-gcc`

`$pacman -S make`

### ForRocketをダウンロード

* ForRocketをgitから落としてForRocketディレクトリに移動

### そのままでもコンパイルできるけど単体で完結したバイナリがほしいね？

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

* excalibarと同じディレクトリに置いてくれたらそれからも使える...と思う 
