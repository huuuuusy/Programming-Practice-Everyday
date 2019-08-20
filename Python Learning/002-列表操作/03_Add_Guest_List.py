""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
任务： 额外邀请三位嘉宾
      以02_Change_Guest_List为基础
        1. 在程序末尾添加一条print语句，指出你找到了一个更大的餐桌
        2. 使用insert()将一位新嘉宾添加到名单开头
        使用insert()将另一位新嘉宾添加到名单中间
        使用append()将最后一位新嘉宾添加到名单末尾
        3. 打印一系列消息，向名单中的每位嘉宾发出邀请
"""

# 邀请嘉宾
guests = ["tom", "maria", "emma"]

def print_guests(guests_list):
    for guest in guests_list:
        name = guest.title()
        print(name + ", Please come to dinner.")

print_guests(guests)

# 第一位嘉宾无法赴约
name = guests[0].title()
print("\nSorry, " + name + " can't make it to dinner.\n")

# 邀请另一位
del(guests[0])
guests.insert(0, "Jack")

# 重新打印
print_guests(guests)

"""新内容"""

# 找到更大的餐桌，添加嘉宾
print("\nWe got a bigger table!\n")
guests.insert(0, "frida")
guests.insert(2, "reinhold")
guests.append("elizabeth")

print_guests(guests)



