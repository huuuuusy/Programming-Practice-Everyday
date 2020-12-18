""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 
工具： python == 3.7.6
介绍： 深度之眼《Python高手之路》项目实战2：电子商城
"""

# user.py为用户信息操作文件

from db import db_handler

def login_interface(name, password):
    # 登录界面
    user_dic = db_handler.select(name)
    if user_dic: # 读取用户的json文件
        if password == user_dic['password'] and not user_dic['locked']:
            return True, '登录成功'
        else:
            return False, '用户密码错误或者用户已经被锁定'
    else:
        return False, '用户不存在'

def lock_user_interface(name):
    # 锁定用户
    user_dic = db_handler.select(name)
    if user_dic:
        user_dic['locked'] = True
        db_handler.save(user_dic)



