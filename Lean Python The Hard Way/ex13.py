# _*_ coding:utf-8 _*_


"""
from-import语句作用
python from import语句也是导入模块的一种方法，更确切的说是导入指定的模块内的指定函数方法。
from-import语句语法:
from module import name
关键字 模块名 关键字 方法名
"""
from sys import argv		# argv 这个参数的值不能自己随便定义，会报错

script,first,second,third = argv
# script 可以改但是没变化 显示的都是脚本的名字,因为赋值的是脚本的地址和名字

print "The script is called:",script
print "Your first variable is:",first
print "Your second varlable is:",second
print "Your third variable is:",third

"""
解包确切含义还学要清理！
文档给的解释：它的含义很简单：“把 argv 中的东西解包，将所有的参数依次赋予从左边开始的变量名
1.给你的脚本三个以下的参数。看看会得到什么错误信息。试着解释一下
ValueError: need more than 3 values to unpack 报错了 提示需要三个以上的值
2.再写两个脚本，其中一个接受更少的参数，另一个接受更多的参数，在参数解包时给它们取一些有意义的变量名。
	1.给两个参数会报错
		参数：123 456
		Traceback (most recent call last):
		File "ex13.2.py", line 4, in <module>
		script,first,second,third = argv
		ValueError: need more than 3 values to unpack
		提示需要三个以上的值
	2.给6个参数
		参数：123 456  123 456 789 456
		Traceback (most recent call last):
		File "ex13.2.py", line 4, in <module>
		script,first,second,third = argv
		ValueError: too many values to unpack
		提示参数太多，太多的值无法打开
3.将 raw_input 和 argv 一起使用，让你的脚本从用户手上得到更多的输入。
	1.第一次：报错，类型错误:不是在字符串格式化期间转换的所有参数
		from sys import argv
		script,first,second,third = argv
		print "your script is:",script
		raw_input("your first %r is:") % first
		raw_input("your second %r is:") % second
		raw_input("your third %r is:") % third
	2.第二次，感觉需要改善，打印出来像字符串
		from sys import argv
		script,first,second,third = argv
		print "your script is:",script
		time1 = raw_input("your first is:")
		time2 = raw_input("your second is:")
		time3 = raw_input("your third is:")
		print("print:",time1,"raw_input",first)
		print("print:",time2,"raw_input",second)
		print("print:",time3,"raw_input",third)
4.记住“模组(modules)”为你提供额外功能。多读几遍把这个词记住，因为我们后面还会用到它。
"""