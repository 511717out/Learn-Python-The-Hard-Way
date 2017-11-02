# _*_ coding:utf-8 _*_

people = 20
cars = 40
buses = 15

# 如果
if cars > people:
   print "We should take the cars"
# 否则如果
elif cars < people:
   print "We should not take the cars"
# 否则
else:
   print "We can't decide."

if buses > cars:
   print "That's too many buses."
elif buses < cars:
   print "Maybe we could take the buses."
else:
   print "We still can't decide."
   
if people > buses:
   print "Alright,let's just take the buses."
else:
   print "Finemlet's stay home then."
   
"""
1.猜想一下 elif 和 else 的功能。
2.将 cars, people, 和 buses 的数量改掉，然后追溯每一个 if 语句。看看最后会打印出什么来。
3.试着写一些复杂的布尔表达式，例如 cars > people and buses < cars。
4.在每一行的上面写注解，说明这一行的功用。
"""