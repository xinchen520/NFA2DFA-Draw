# NFA2DFA-Draw
这个脚本是用来画 [NFA2DFA](https://github.com/xinchen520/NFA2DFA) 执行后输出的DFA.

## Prerequisites
此脚本用python编写,请先安装python.

此脚本需要安装`networkx`,`pydot` 库,你可以用以下命令安装.
```
pip install networkx 
pip install pydot
```
另外,还需要安装graphviz, 你可以到 [这里](https://www.graphviz.org/download/) 下载对应你的平台的安装程序. 安装完成后,需要将graphviz的bin目录加入
`PATH`环境变量.

比如我的graphviz安装在`C:\Program Files (x86)\Graphviz`下, 那么我需要把`C:\Program Files (x86)\Graphviz\bin`加入`PATH`环境变量中.

## Usage

当你用NFA2DFA把NFA转换成DFA后, 例如, 输入了以下命令后

```
NFA2DFA < input.txt > output.csv
```

这时你会得到一个`output.csv`文件, 然后用以下命令执行脚本

```
python draw_dfa.py output.csv
```

若脚本执行成功, DFA图像将会写入`output.csv.png`文件中.

注意: 本脚本输出的图像中的可能包含不可到达的状态,请自己识别.
