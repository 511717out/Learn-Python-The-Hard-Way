# _*_ coding:utf-8 _*_

"""
from-import语句作用
python from import语句也是导入模块的一种方法，更确切的说是导入指定的模块内的指定函数方法。
from-import语句语法:
from module import name
关键字 模块名 关键字 方法名
"""
# 调用sys模块中的argv函数方法
from sys import argv
# 解包从左往右赋值
script,filename = argv
# 打印输出
print "Wh're going to erase %r." % filename
# 打印输出
print "If you don't want,hit CTRL-c (^c)."
# 打印输出
print "If you do want that,hit RETURN."

# 用户输入 回车继续
raw_input("?")

# 打印输出
print "Opening the file..."
# 读取并执行写入模式并赋值 w 如果存在则覆盖，不存在则新建
target = open(filename,'w')

# 打印输出
print "Truncating the file. Goodbye!"
# 清空target中的文件内容？
# 没有参数也就是从当前位子截断，当前位子新建的文件本来就是空也算是清空吧
target.truncate()
# 打印输出
print "Now I'm going to ask you for three lines."
# 用户输入
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
# 打印输出
print "I'm going to write these to the file."

# 将用户输入的内容写入文件并输出
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
file = target.write(line1 + '\n' + line2 + '\n' + line3)

# 打印输出
print "And finally,we close it."
# 保存并关闭文件
target.close()

"""
write() 方法用于向文件中写入指定字符串。
在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。所以在文件结尾加上close方法关闭并保存文件
1.如果你觉得自己没有弄懂的话，用我们的老办法，在每一行之前加上注解，
为自己理清思路。就算不能理清思路，你也可以知道自己究竟具体哪里没弄明白。
	1.target.truncate()这段代码在这里起的什么作用，删除了在运行程序也没什么变化
	已经理解，起到清空的作用
	2.test.txt 这个文件在内存里到底是怎么创建的，那段代码是创建的命令
	已经理解， w 写入模式如果文件存在则覆盖 不存在则创建
2.写一个和上一个练习类似的脚本，使用 read 和 argv 读取你刚才新建的文件。
	from sys import argv
	script,name = argv
	print "Print the name of the output %r file" % name
	test = open(name)
	print test.read()
3.文件中重复的地方太多了。试着用一个 target.write() 
将 line1, line2, line3 打印出来，你可以使用字符串、格式化字符、以及转义字符。
	file = target.write(line1 + '\n' + line2 + '\n' + line3)
4.找出为什么我们需要给 open 多赋予一个 'w' 参数。
提示： open 对于文件的写入操作态度是安全第一，所以你只有特别指定以后，它才会进行写入操作
	#open(路径+文件名,读写模式)
"""