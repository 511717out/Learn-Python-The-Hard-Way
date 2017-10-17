# _*_ c0ding:utf-8 _*_

# raw_input 用户输入
print "How old are you",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So,you're %r old, %r tall and %r heavy." % (
	age,height,weight)
# 和转义序列有关的，想想为什么最后一行 '6\'2"' 里边有一个 \' 序列。单引号需要被转义，从而防止它被识别为字符串的结尾。
