""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
任务： 创建一个至少包含5个用户名的列表，且其中一个用户名为'admin'; 在每位用户登录网站后都打印一条问候消息
      遍历用户名列表，并向每位用户打印一条问候消息：
        1. 如果用户名为'admin'，就打印一条特殊的问候消息，如Hello admin, would you like to see a status report?
        2. 否则，打印一条普通的问候消息，如Hello Eric, thank you for logging in again
"""

usernames = ['eric', 'willie', 'admin', 'erin', 'ever']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again!")