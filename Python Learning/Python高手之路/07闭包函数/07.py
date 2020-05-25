""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 
工具： python == 3.7.6
介绍： 深度之眼《Python高手之路》作业07：闭包函数
"""

import random
import time

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

def hw2():
    user_data = {
    'user': None,
    'login': False,
    'now_time': time.time()
    }
    db_username = 'albert'
    db_password = '123'
    
    def auth(func):
        def wrapper(*args, **kwargs):
            passed_time = time.time()-user_data['now_time'] # 计算距离上次登录成功的时间

            if user_data['user'] and passed_time < 3: # 如果存在用户且距离上次成功时间小于指定时长
                return func(*args, **kwargs)
            else:
                while True: # 进入登录环节
                    username = input('input your username>>: ').strip()
                    password = input('input your password>>: ').strip()
                    if username == db_username and password == db_password:
                        print('login successfully!')
                        user_data['user'] = username
                        user_data['login'] = True
                        user_data['now_time'] = time.time()
                        return func(*args, **kwargs)
                    else:
                        print('username or password is invalid')
        return wrapper
        
    @auth
    def index():
        print('This is index page')
    
    @auth
    def home(name):
        print('Welcome %s to home page' % name)
    
    index()
    time.sleep(random.randint(2, 4)) # 让系统随机休眠2-4秒
    home('albert')

"""
练习三
编写日志装饰器，实现功能：一旦某函数执行，则将函数执行时间写入到日志文件中，日志文件路径可以指定。
注意：时间格式的获取
"""
def hw3():
    def add_log(file):
        def wrapper(func):
            def inner(*args, **kwargs):
                with open(file, 'a', encoding='utf-8') as f:
                    f.write('[%s]:[%s]\n' % (func.__name__, time.strftime('%Y-%m-%d %X')))
                    return func(*args, **kwargs)
            return inner           
        return wrapper

    @add_log('db1.txt')
    def index():
        print('This is index page')
    
    @add_log('db2.txt')
    def home(name):
        print('Welcome %s to home page' % name)
    
    index()
    home('albert')

if __name__ == "__main__":
    #hw1()
    #hw2()
    hw3()
                