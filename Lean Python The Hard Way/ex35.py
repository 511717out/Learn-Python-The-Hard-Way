# _*_ coding:utf-8 _*_

"""
exit(0)：无错误退出
exit(1)：有错误退出
"""

from sys import exit

def gold_room():
   print "This room is full of gold. How much do you take?"
   
   next = raw_input("> ")
   # 原判断代码：
   # if "0" in next or "1" in next:
      # how_much = int(next)
   # else:
	    # dead("Man,learn to type a number.")
	# 修改以后的判断
	try:
	   how_much = int(next)
	except:
	   dead("Wrong input.")
   if how_much < 50:
      print "Nice,you're not greedy,you win"
      exit(0)
   else:
      dead("You greedy bastard!")

def bear_room():
   print "There is a bear here."
   print "The baer has a bunch of honey."
   print "The fat bear is in front of anther door."
   print "How are you going to move the bear?"
   bear_moved = False
   
   while True:
      next = raw_input("> ")
      if next == "take honey":
         dead("The bear looks at you then slaps you face off.")
      elif next == "taunt bear" and not bear_moved:
         print "The bear has moved from the door.you can go through it now."
         bear_moved = True
      elif next == "taunt bear" and bear_moved:
         dead("The bear gets pissed off and chews your leg off.")
      elif next == "open door" and bear_moved:
         gold_room()
      else:
         print "I got no idea what that means."

def cthulhu_room():
   print "Here you see the great evil Cthulhu."
   print "He it, whatever stares at you and you go insane."
   print "Do tou flee for your life or eat your head?"
   
   next = raw_input("> ")
   
   if "flee" in next:
      start()
   elif "head" in next:
      dead("Well that was tasty!")
   else:
      cthulhu_room()
		
		
def dead(why):
   print why,"Good job!"
   exit(0)
   
def start():
   print "you are in a dark room."
   print "There is a door to your right and left."
   print "Which one do you take?"
   
   next = raw_input()
   
   if next == "left":
      bear_room()
   elif next == "right":
      cthulhu_room()
   else:
      dead("You stumble around the room until you starve.")

start()


"""
# _*_ coding:utf-8 _*_

from sys import exit

def gold_room():
        # 这个房间里装满了金子。你要花多少钱
    print "This room is full of gold.  How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
	         # 人，学会打字
        dead("Man, learn to type a number.")

    if how_much < 50:
	          # 很好，你不是贪婪，你赢了
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
	         # 你贪婪的混蛋
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here." # 这里有一只熊
    print "The bear has a bunch of honey." # 这只熊有一堆蜂蜜
    print "The fat bear is in front of another door."# 那只肥熊在另一扇门前
    print "How are you going to move the bear?" # 你打算如何移动这只熊
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey": # 把蜂蜜
            dead("The bear looks at you then slaps your face off.") # 熊看着你，然后把你的脸给打了
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now." # 熊已经从门上走了。现在就可以完成了
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.") # 熊被激怒了，你的腿被咬掉了
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means." # 我不知道那是什么意思


def cthulhu_room():
    print "Here you see the great evil Cthulhu." # 在这里，你看到了伟大的Cthulhu
    print "He, it, whatever stares at you and you go insane." # 他，不管你盯着你什么，你都疯了
    print "Do you flee for your life or eat your head?" # 你是为了你的生命逃跑还是为了吃你的头

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!") # 这是美味的
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room." # 你在一个黑暗的房间里
    print "There is a door to your right and left." # 你的左右手有一扇门
    print "Which one do you take?" # 你选哪一个

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.") # 你在房间里跌跌撞撞地走，直到你饿死


start()
"""