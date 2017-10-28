# _*_ coding:utf-8 _*_


"""
file.seek(offset[, whence])
seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。
如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。
设置文件当前位置
参考文档：http://www.runoob.com/python/file-seek.html
"""
# 从sys库中导入argv方法
from sys import argv
# 从argv中读取script，input_file
script,input_file = argv
# 定义方法：打印全部文件
def print_all(f):
   print f.read()
# 定义方法把指针放到第一行
# 因为print_all方法把文件读取完了，需要把指针指回文件的开始位子
# 如果不设定的话第三个方法中的readline()无法正常工作
def rewind(f):	
   # file.seek(offset[, whence])
   #设置文件指针为当前位置
   f.seek(0)

# 定义方法：逐行打印行号和该行内容
def print_a_line(line_count,f):
   print line_count,f.readline()

# 打开文件
current_file = open(input_file)

# 使用方法：打印全部文件
print "First let's print ths whole file:\n"
print_all(current_file)

#使用方法把指针放到第一行
print "Now let's rewind,kind of linke a tape."
rewind(current_file)
# 定义方法：逐行打印行号和该内容
print "Let's print three lines:"
current_line = 1
print_a_line(current_line,current_file)
current_line = current_line + 1
print_a_line(current_line,current_file)
current_line = current_line + 1
print_a_line(current_line,current_file)

"""
1.通读脚本，在每行之前加上注解，以理解脚本里发生的事情。
2.每次 print_a_line 运行时，你都传递了一个叫 current_line 的变量。
在每次调用函数时，打印出 current_line 的至，跟踪一下它在 print_a_line 中是怎样变成 line_count 的
	每次运行print_a_line时只是把current_line的值赋到line_count上
3.找出脚本中每一个用到函数的地方。检查 def 一行，确认参数没有用错。
4.上网研究一下 file 中的 seek 函数是做什么用的。试着运行 pydoc file 看看能不能学到更多。
	参考文档：http://www.runoob.com/python/file-seek.html
5.研究一下 += 这个简写操作符的作用，写一个脚本，把这个操作符用在里边试一下。

"""