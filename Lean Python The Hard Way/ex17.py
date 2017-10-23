# _*_ coding:utf-8 _*_

# 调用sys模块中的argv函数
from sys import argv
# 调用os.path模块中的exista函数
# 这个命令将文件名字符串作为参数，如果文件存在的话，它将返回 True，否则将返回 False。
# os.path通用路径操作，
# 官方文档:https://docs.python.org/2.7/library/os.path.html#os.path.splitunc
from os.path import exists

# 解包并从左往右赋值
script,from_file,to_file = argv

# 打印输出
print "Copying from %s to %s" % (from_file,to_file)

# we could do these two on one line too,how?
# 打开文件并赋值 默认是只读模式
input = open(from_file)
# 执行input.read读取文件
indata = input.read()
# 打印输出
print "The input file is %d bytes long" % len(indata)

# 打印输出
print "Does the output file exist? %r" % exists(to_file)
# 打印输出
print "Ready,hit RETURN to continue,CTRL-C to abort."
# 用户输入
raw_input()

# 读取并执行写入模式，赋值
output = open(to_file,'w')
# 写入文件
output.write(indata)
# 打印输出
print "Alright,all done."
# 保存并关闭文件
output.close()
# 保存并关闭文件
input.close()


"""
1.再多读读和 import 相关的材料，将 python 运行起来，试试这一条命令。
试着看看自己能不能摸出点门道，当然了，即使弄不明白也没关系。
2.这个脚本 实在是 有点烦人。没必要在拷贝之前问一遍把，没必要在屏幕上输出那么多东西。
试着删掉脚本的一些功能，让它使用起来更加友好。
	可以把输入输出语句注释掉
3.看看你能把这个脚本改多短，我可以把它写成一行
	from sys import argv
	from os.path import exists
	script,from_file,to_file = argv
	open(to_file,'w').write(open(from_file).read())
	# 我可以写成这样
	4.我使用了一个叫 cat 的东西，这个古老的命令的用处是将两个文件“连接(con*cat*enate)”到一起，
	不过实际上它最大的用途是打印文件内容到屏幕上。你可以通过 man cat 命令了解到更多信息。
	5.使用 Windows 的同学，你们可以给自己找一个 cat 的替代品。
	关于 man 的东西就别想太多了，Windows 下没这个命令。
	1.cat：查看文件的内容、连接文件、创建一个或多个文件和重定向输出到终端或文件  用法：cat [选项] [文件]
	2.cat的代替品type，type()就是一个最实用又简单的查看数据类型的方法，先简单理解成打印东西到屏幕吧
6.找出为什么你需要在代码中写 output.close() 。
	1.先这样理解。不对的以后学了再改
	程序运行结束后 保存的文件并没有保存在磁盘中而是缓存在内存中 
	使用close()关闭文件后 会把关闭此文件把内存中缓存的文件保存在内存中，
	close()方法关闭打开的文件。调用此方法后将无法读取或写入封闭文件。
	、任何需要打开该文件的操作将在文件关闭后引发ValueError。允许多次调用close()。
	当文件的引用对象重新分配给另一个文件时，Python会自动关闭一个文件。 
	使用close()方法关闭文件是个好习惯。
"""