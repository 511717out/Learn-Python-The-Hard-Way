# _*_ coding:utf-8 _*_

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "NOt many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"
   
dogs +=5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less then or quual to dogs."
	
if people == dogs:
    print "People wre dogs"
	
	



"""
1.你认为 if 对于它下一行的代码做了什么？
if进行条件判断结果为True则继续执行
2.为什么 if 语句的下一行需要 4 个空格的缩进？
因为优先等级
3.如果不缩进，会发生什么事情？
会报错
4.把习题 27 中的其它布尔表达式放到``if语句``中会不会也可以运行呢？试一下。
5.如果把变量 people, cats, 和 dogs 的初始值改掉，会发生什么事情？
条件判断的结果发生了变化
"""