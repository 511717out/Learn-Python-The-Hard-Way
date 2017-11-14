"""
and
与

del
删除列表里面的元素

from
用来导入模块和包
not
非

while
while循环

as
如果想要改变被导入模组在当前模组中的名称，而不是sys.modules中的名称。可以使用import as，
import some as other
print(other.name)

和	

import some
other = some
del some
print(other.name)

elif
if循环里面的语句

global
在函数中定义全局变量
https://www.cnblogs.com/ganlan/p/5114083.html

or
或
with
with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，
释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等。
https://www.cnblogs.com/zhangkaikai/p/6669750.html
更专业
https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/

assert
python assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假。可以理解assert断言语句为raise-if-not，用来测试表示式，其返回值为假，就会触发异常。
assert的异常参数，其实就是在断言表达式后添加字符串信息，用来解释断言并更好的知道是哪里出了问题。格式如下：
assert expression [, arguments]
assert 表达式 [, 参数]
assert len(lists) >=5,'列表元素个数小于5'
assert 2==1,'2不等于1'

else
if判断
if
if判断
pass
主要用于if判断语句中，意思是什么都不做

yield
yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。
简要理解：yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。

break
跳出整个循环语句 一般用于循环语句中

except
try  except 程序异常处理

import
用来导入模块的，可以出现在程序的任何位子

print
打印输出

class
定义类 
语法是class 后面紧接着，类的名字，最后别忘记“冒号”，这样来定义一个类。

exec
执行语句

in
如果在指定的序列中找到值返回 True，否则返回 False。

raise
https://www.cnblogs.com/Lival/p/6203111.html
在Python中，要想引发异常，最简单的形式就是输入关键字raise，
https://www.cnblogs.com/caicaihong/p/6402245.html

continue
结束本次循环进行下一次循环

finally
https://www.cnblogs.com/Lival/p/6203111.html
try...finally 无论异常是否发生，在程序结束前finally中的语句都会被执行。

is
==比较操作符：用来比较两个对象是否相等，value做为判断因素；
is同一性运算符：比较判断两个对象是否相同，id做为判断因素

return
return会返回一个参数或者是值

def
定义一个函数

for
for循环

lambda
可以这样认为,lambda作为一个表达式，定义了一个匿名函数，上例的代码x为入口参数，x+1为函数体。在这里lambda简化了函数定义的书写形式。是代码更为简洁，但是使用函数的定义方式更为直观，易理解。
https://www.cnblogs.com/AlwaysWIN/p/6202320.html



try

异常处理语句
"""