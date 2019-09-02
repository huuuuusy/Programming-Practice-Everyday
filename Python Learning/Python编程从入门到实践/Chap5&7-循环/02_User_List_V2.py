""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
任务： 在01_User_List基础上加一条if语句，检查用户名列表是否为空
        1. 如果为空，就打印消息We need to find some users!
        2. 删除列表中的所有用户名，核实将打印正确的消息
"""

def check_usernames(usernames):
    if usernames:
        for username in usernames:
            if username == 'admin':
                print("Hello admin, would you like to see a status report?")
            else:
                print("Hello " + username + ", thank you for logging in again!")
    else:
        print("We need to find some users!")

usernames = ['eric', 'willie', 'admin', 'erin', 'ever']
check_usernames(usernames)

for i in range(0, len(usernames)):
    del(usernames[0])

print("\n Check usernames again:\n")
check_usernames(usernames)