# _*_ coding:utf-8 _*_


# %r 优先用repr()函数进行字符串转换
# %s 优先使用str()函数进行字符串转换
# %d 转成有符号的十进制数

# 定义变量赋值
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# 多个参数需要加括号变量和变量之间用逗号隔开
y = "Those who know %s and those who %s." % (binary,do_not)

# 打印输出
print x
print y

print "I asid: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a tight side"

# 加号链接两个字符串输出
print w + e