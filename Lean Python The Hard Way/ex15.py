# _*_ coding:utf-8 _*_

"""
from-import语句作用
python的 from import语句也是导入模块的一种方法，更确切的说是导入指定的模块内的指定函数方法。
from-import语句语法:
from module import name
关键字 模块名 关键字 方法名
"""
# 从sys这个库中取出argv这个方法，
from sys import argv
# 将argv解包然后依次赋值给从左往右的变量
script, filename = argv
# 打开赋值给变量txt的文件名，这里的文件名是ex15_sample.py
txt = open(filename)
# 打印输出语句，里面用了%r原样输出意思
print "Here's you file %r:" % filename
# 执行txt的read方法读取并输出
print txt.read()
# 输出语句
print "Type the filename again:"
# 获取用户输入的信息，并赋值给变量file_again
file_again = raw_input("> ")
# open方法打开file_again文件并赋值给变量txt_again
txt_again = open(file_again)
# 执行txt的read方法读取并输出
print txt_again.read()


"""
1.在每一行的上面用注解说明这一行的用途。
	ok
2.如果你不确定答案，就问别人，或者上网搜索。大部分时候，
只要搜索 “python” 加上你要搜的东西就能得到你要的答案。比如搜索一下“python open”。

3.我使用了“命令”这个词，不过实际上它们的名字是“函数（function）”和“方法（method）。
上网搜索一下这两者的意义和区别。看不明白也没关系，迷失在别的程序员的知识海洋里是很正常的一件事情。
	1.网上搜索出来的答案，不理解的和错误解释的后面懂了在来修改：
		函数是一段代码，通过名字来进行调用。它能将一些数据（参数）传递进去进行处理，然后返回一些数据（返回值），也可以没有返回值。

		所有传递给函数的数据都是显式传递的。

		方法也是一段代码，也通过名字来进行调用，但它跟一个对象相关联。方法和函数大致上是相同的，但有两个主要的不同之处：

		1.方法中的数据是隐式传递的；
		2.方法可以操作类内部的数据（请记住，对象是类的实例化–类定义了一个数据类型，而对象是该数据类型的一个实例化）
		补上:方法可以操作已在类中声明的私有实例（成员）数据。其他代码都可以访问公共实例数据。
		以上只是简略的解释，忽略了作用域之类的问题。
4.删掉 10-15 行使用到 raw_input 的部分，再运行一遍脚本。
	1.错误信息
		Here's you file 'ex15_sample.txt':
		This is stuff I typed into a file.
		It is really cool stuff.
		Lots and lots of fun to have in here.
		Type the filename again:
		Traceback (most recent call last):
		File "ex15.py", line 18, in <module>
		txt_again = open(file_again)
		NameError: name 'file_again' is not defined
		只打印输出一遍ex15_sample.txt中的文件 并报错file_again名称错误没有定义
		因为open方法打开的变量file_again没有定义
5.只是用 raw_input 写这个脚本，想想那种得到文件名称的方法更好，以及为什么
	!! 是这样吗？需要后续补充
		from sys import argv
		script, filename = argv
		txt = open(filename)
		print "Here's your file %r:" % filename
		print txt.read()
		print "Type the filename again:"
		txt_again = open(raw_input("> "))
		print txt_again.read()
6.运行 pydoc file 向下滚动直到看见 read() 命令（函数/方法）。
看到很多别的命令了吧，你可以找几条试试看。不需要看那些包含 __ （两个下划线）的命令，
这些只是垃圾而已。
	read.()      读取整个文件
	readline.()  读取下一行
	readlines.() 读取整个文件到一个迭代器以供我们遍历（读取到一个list中，以供使用，比较方便）、
	如果忘了直接百度搜索使用的方法
7.再次运行 python 在命令行下使用 open 打开一个文件，这种 open 和 read 的方法也值得你一学。
	完成
	>ex15.2.py
	dvdfvkhfdvbkjdf
	fdbvfdhviusfdhvui
	dvfdvfdsvsdfvsdfv
8.让你的脚本针对 txt and txt_again 变量执行一下 close() ，
处理完文件后你需要将其关闭，这是很重要的一点。
	1.close() 方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 
	否则会触发 ValueError 错误。 close() 方法允许调用多次。
	2.当 file 对象，被引用到操作另外一个文件时，Python 会自动关闭之前的 file 对象。 
	使用 close() 方法关闭文件是一个好的习惯。

"""