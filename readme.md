まずMSYS2をインストールする（https://www.msys2.org/）
したらMSYS2 MinGW-64bitでターミナルをひらいて
次に、gccとmakeをインストール
$pacman -Sy
$pacman -Su
$pacman -S mingw-w64-x86_64-gcc
$pacman -S make
ForRocketをgitから落としてForRocketディレクトリに移動
makefileのコンパイラオプションの項目を編集してMSYSから呼び出されるdllファイルを3つ静的リンク
## Compiler Option
####################################
CXXFLAGS=-Wall -std=gnu++11 -static -lstdc++ -lgcc -lwinpthread
RELEASE_FLAGS=-O2
TEST_FLAGS=-O0 -g -DDEBUG
そしたらターミナルに戻って
$make release
binディレクトリにForRocket.exeができるので好きなところに移動してpowershellかコマンドプロンプトでつかう
