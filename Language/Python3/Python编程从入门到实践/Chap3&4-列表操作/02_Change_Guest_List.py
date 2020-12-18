""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
任务： 得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾
      以01_Guest_List为基础
        1. 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名
        2. 再次打印一系列消息，将名单中的每位嘉宾发出邀请
"""

# 邀请嘉宾
guests = ["tom", "maria", "emma"]

def print_guests(guests_list):
    for guest in guests_list:
        name = guest.title()
        print(name + ", Please come to dinner.")

print_guests(guests)

"""新内容"""

# 第一位嘉宾无法赴约
name = guests[0].title()
print("\nSorry, " + name + " can't make it to dinner.\n")

# 邀请另一位
del(guests[0])
guests.insert(0, "Jack")

# 重新打印
print_guests(guests)


