# _*_ coding:utf-8 _*_

# 注意写代码时不要tab键和空格键一起用
# 定义函数cheese_and_crackers 并给出两个参数
def cheese_and_crackers(cheese_count,boxes_of_crackers):
   # 打印输出
   print "you have %d cheese!" % cheese_count
   # 打印输出
   print "you have %d boxes of crackers!" % boxes_of_crackers
   # 打印输出
   print "Man that's enough for a party!"
   # 打印输出
   print "Get a blanket.\n"
#打印输出
print "We can just give the funcyion numbers directly:"
# 给出参数用来传递参数值
cheese_and_crackers(20,30)

# 打印输出
print "OR'we can use variables from our script:"
# 定义变量
amount_of_cheese = 10
#定义变量
amount_of_crackers = 50

# 传递参数值
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# 打印输出
print "We can ever do math iside too:"
# 计算并传参
cheese_and_crackers(10 + 20,5 + 6)

# 打印输出
print "And we can combine the two,variables and math:"
# 变量计算并传参
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)


"""
1倒着将脚本读完，在每一行上面添加一行注解，说明这行的作用。
2.从最后一行开始，倒着阅读每一行，读出所有的重要字符来。
3.自己编至少一个函数出来，然后用10种方法运行这个函数。
ex19.1.py
"""