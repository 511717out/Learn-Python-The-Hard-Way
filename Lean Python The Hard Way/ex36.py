#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
游戏人物设定：
诸葛亮，刘备，曹操，貂蝉，大乔，小乔。


房间1会进入房间3
房间2会进入房间4
房间3
房间4
房间5



"""


def house1(parameter):
    print("欢迎 %r 来到魔法城堡" % parameter)
    list_1 = ["诸葛亮", "刘备","曹操"]
    list_2 = ["貂蝉", "大乔", "小乔"]
    if parameter in list_1:
       time1 = input("你遇到了大美女貂蝉，A 调戏 B 不调戏")
       if time1 == "A":
           print("因为你长得太丑了，貂蝉打了你一巴掌，并拨打了110，你逃走了")
           house4(parameter)
       elif time1 == "B":
           print("你触发的系统的自卑属性，系统提示：自古英雄爱美人,不过没关系，系统判定你是一个意志坚定的人，系统赠送你武功秘籍'葵花宝典'")
           house5(parameter)
       else:
           print("对不起，你在此房间只有以上两个选择！")
           house1()
    elif parameter in list_2:
       time2 = input("恭喜你哦！你遇到了大帅锅诸葛亮！A 调戏 B 不调戏 ")
       if time2 == "A":
           print("恭喜你！英雄配美人获得系统奖励，并进入两人世界。")
           house3(parameter)
       elif time2 == "B":
           print("建议你还是调戏一下，不过没关系，你被系统强制调戏了一下诸葛亮，并进入两人世界")
           house3(parameter)
       else:
           print("对不起，你在此房间只有以上两个选择！")
           house1()

    else:
       house1()
def house2(parameter2):
    print("系统发放给你的初始装备是：一个面包，一个苹果，一根香蕉。")
    print("你往你的前方走了一个小时，正在这时你看到了一个小孩，他说他快到饿死了，想让你救救他。")
    aaa = input("A救 B不救")
    if aaa == "A":
        print("你壮烈的牺牲了，因为他是基地组织的成员，你看到了他的真实面容")
        exit(0)
    elif aaa == "B":
        print("你并没有救他 恭喜你，你成功的度过了第一个考验!但是很不辛，在这里你只有死亡，这个房间并没有成活的机会")
        exit(0)
def house3(parameter3):
    print("%s 诸葛亮，欢迎你们来到爱的世界！") % parameter3
    print("可惜的是系统只是还没有完善的电脑，你并没有体会的爱的味道！")
    exit(0)
def house4(parameter4):
    print("%s 欢迎来到大冒险! 在这里你将体验不一样的人生")
    print("你被系统扔到了非洲的难民集中地，你需要靠自己的能力度过未来的3年美好时光")
    house2(parameter4)

def house5(parameter5):
    print(" %s 欢迎来到修炼室！在这里你将成为一代宗师！成就你独霸江湖的梦想。") % parameter5
    print("你经历了九九八十一难之后终于练成葵花宝典，恭喜你！没有奖励")
    exit(0)


def entrance():

    print("诸葛亮，刘备，曹操，貂蝉，大乔，小乔")
    Character_name = input("请选择你喜爱的人物：")
    list_1 = ["诸葛亮", "刘备", "曹操", "貂蝉", "大乔", "小乔"]
    if Character_name in list_1:
        print("请选择你要进入的房间")
        name1 = input("1,2,3,4,5:>")
        name1 = int(name1)
        if name1 == 1:
           house1(Character_name)
        else:
            print("不好意思！你没有选择的权利，只能进入1号房间")
            entrance()
    else:
        entrance()
entrance()



