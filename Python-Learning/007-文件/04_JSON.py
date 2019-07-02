""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

任务：
利用json保存和读取用户生成的数据
"""

import json

# 打开json文件，读取已经存储的用户名
def get_stored_username():
    filename = 'data/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
# 存储新的用户名
def get_new_username():
    username = input("What is your name? ")
    filename = 'data/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

# 判定用户类型
def greet_user():
    username = get_stored_username()
    if username:
        correct = input("Are you " + username + "? (y/n) ")
        if correct == 'y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
