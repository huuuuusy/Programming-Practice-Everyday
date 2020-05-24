""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 
工具： python == 3.7.6
介绍： 深度之眼《Python高手之路》作业07：闭包函数
"""

"""
练习一
编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）。
要求：登录成功一次，后续的函数都无需再输入用户名和密码；注意：从文件中读出字符串形式的字典，可以用以下方式把字典字符串转化成字符串
eval('{"name":"albert","password":"123"}')
"""
def hw1():
    db = 'a.txt'
    login_status = {'status': False}

    def auth(auth_type='file'):
        def auth2(func):
            def wrapper(*args, **kwargs):
                if login_status['status']: # 如果已经登录，将直接返回上层函数的结果
                    return func(*args, **kwargs)
                if auth_type == 'file': # 如果未登录，则读取已有数据库文件进行登录判定
                    with open(db, encoding='utf-8') as f:
                        dic = eval(f.read())
                    name = input('username: ').strip()
                    password = input('password: ').strip()
                    if name == dic['name'] and password == dic['password']:
                        login_status['status'] = True
                        return func(*args, **kwargs)
                    else:
                        print('username or password error')
                elif auth_type == 'sql':
                    pass
                else:
                    pass
            return wrapper
        return auth2

    @auth()
    def index(): # 第一次调用，如果本次登录成功则后续无需再登录
        print('index')

    @auth(auth_type='file') # 第二次调用，因为已经修改登录状态，所以无需再登录
    def home(name):
        print('welcome %s to home' % name)

    index()
    home('albert')

"""
练习二
编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录
"""
import time
import random

def hw2():
    user_data = {
    'user': None,
    'login': False,
    'now_time': time.time()
    }
    db_username = 'albert'
    db_password = '123'
    
    pass

if __name__ == "__main__":
    #hw1()
    hw2()
                