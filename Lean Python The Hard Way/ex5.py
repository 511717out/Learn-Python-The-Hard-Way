# _*_ coding:utf-8 _*_

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# 相当于C语言里的printf()的字符串格式化
# %s 优先用str()函数进行字符串转换输出
print "Let's talk about %s." % my_name
# 转成有符号十进制数输出
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky,try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	my_age,my_height,my_weight,my_age + my_height + my_weight )
print "_______________________________________________________________________________"

name = 'Zed A. Shaw'
time = 23 # int 
master = 'A' # char
age = 35 # not a lie
height = 74 # lnches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "les's talk abput %s." % name
print "les's talk abput %r." % name
# print "les's talk abput %c." % name   # 需要字符串为int类型或者char
print "les's %c talk abput %c." % (time,master)
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth
# this lins is tricky,try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age,height,weight,age + height + weight )
print "=============================================================="

# 试着使用变量将英寸和磅转换成厘米和千克。不要直接键入答案。使用 Python 的计算功能来完成。
inch = int(raw_input()) # 输入英寸
kg = int(raw_input())  # 输入磅
inch = inch * 0.45 # 转换成cm
kg = kg * 0.45  # 转换kg
print inch
print kg