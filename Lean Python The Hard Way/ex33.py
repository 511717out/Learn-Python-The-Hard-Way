# _*_ coding:utf-8 _*_

i = 0
numbers = []

while i < 6:
   print "At the top i is %d" % i
   # append() 方法用于在列表末尾添加新的对象。
   numbers.append(i)
   
   i = i + 1
   print "Numbers now: ",numbers
   print "At the bottom i is %d" % i
   
print "The numbers: "
for num in numbers:
   print num


   
"""
1.将这个 while 循环改成一个函数，将测试条件(i < 6)中的 6 换成一个变量。
ok ex33.1.py
2.使用这个函数重写你的脚本，并用不同的数字进行测试。
ok
3.为函数添加另外一个参数，这个参数用来定义第 8 行的加值 + 1 ，这样你就可以让它任意加值了。
ok
4.再使用该函数重写一遍这个脚本。看看效果如何。
ok
5.接下来使用 for-loop 和 range 把这个脚本再写一遍。你还需要中间的加值操作吗？如果你不去掉它，会有什么样的结果？
ok ex33.2.py   需要加值操作  不去掉是正常的
"""