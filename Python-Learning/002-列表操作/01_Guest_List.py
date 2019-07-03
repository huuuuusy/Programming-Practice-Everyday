""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
任务： 嘉宾名单
        1. 创建一个列表，其中包含至少3个嘉宾
        2. 使用这个列表打印邀请信息
"""

# 邀请嘉宾
guests = ["tom", "maria", "emma"]

for guest in guests:
    name = guest.title()
    print(name + ", Please come to dinner.")