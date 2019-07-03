""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
任务： 模拟网站确保每位用户的用户名都独一无二的方式
        1. 创建一个至少包含5个用户名的列表，并将其命名为current_users
        2. 再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表current_users中
        3. 遍历列表new_users，对于其中的每个用户名，都检查它是否已被使用
        如果是这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用
        4. 确保比较是不区分大小写；换句话说，如果用户名'John'已被使用，应拒绝用户名'JOHN'
"""

current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

current_users = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great " + new_user + ", that name is available")