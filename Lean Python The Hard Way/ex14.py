# _8_ coding:utf-8 _*_

from sys import argv
script,user_name,age = argv
prompt = '='

print "Hi %s I'm the %s script." % (user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "How old are you %s?" % age
age_1 = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright,so you said %r about liking me.
You're as big as me %r Are 20 years old.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes,age_1,lives,computer)

"""
1.查一下 Zork 和 Adventure 是两个怎样的游戏。 看看能不能下载到一版，然后玩玩看。
	后续下载
2.将 prompt 变量改成完全不同的内容再运行一遍
	改成：prompt '='
	用户输入前边的>号会变成等号
3.给你的脚本再添加一个参数，让你的程序用到这个参数
	加上年龄：script,user_name，age = argv
4.确认你弄懂了三个引号 \"\"\" 可以定义多行字符串，而 % 是字符串的格式化工具。
"""