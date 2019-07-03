""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
任务： 新购买的餐桌无法及时送达，因此只能邀请两位嘉宾
      以03_Add_Guest_List为基础
        1. 在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息
        2. 使用pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止
        每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐
        3. 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在邀请之列
        4. 使用del将最后两位嘉宾从名单中删除，让名单变成空的
        打印该名单，核实程序结束时名单确实是空的
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

# 找到更大的餐桌，添加嘉宾
print("\nWe got a bigger table!\n")
guests.insert(0, "frida")
guests.insert(2, "reinhold")
guests.append("elizabeth")

print_guests(guests)

"""新内容"""

# 餐桌无法送达
print("\nSorry, we can only invite 2 people to dinner.\n")

for i in range(0, 4):
    name = guests.pop()
    print("Sorry " + name.title() + ", there is no room at the table.")

# 向最后2人发出邀请
print("\n")
print_guests(guests)

# 清空名单
for i in range(0, len(guests)):
    del(guests[0])

print(guests)