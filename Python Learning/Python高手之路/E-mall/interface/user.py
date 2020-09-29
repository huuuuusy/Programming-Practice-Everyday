from db import db_handler
from lib import common

user_logger = common.get_logger('user')


def login_interface(name, password):
    user_dic = db_handler.select(name)
    if user_dic:
        if password == user_dic['password'] and not user_dic['locked']:
            return True, '登陆成功'
        else:
            return False, '用户密码错误或已经锁定'
    else:
        return False, '用户不存在'


def register_interface(name, password, balance=15000):
    user_dic = db_handler.select(name)
    if user_dic:
        return False, '用户已经存在'
    else:
        user_dic = {'name': name,
                    'password': password,
                    'balance': balance,
                    'credit': balance,
                    'locked': False,
                    'bankflow': [],
                    'shoppingcart': {}}
        db_handler.save(user_dic)
        user_logger.info('%s 注册了' % name)
        return True, '注册成功'


def lock_user_interface(name):
    user_dic = db_handler.select(name)
    if user_dic:
        user_dic['locked'] = True
        db_handler.save(user_dic)


def un_lock_user_interface(name):
    user_dic = db_handler.select(name)
    if user_dic:
        user_dic['locked'] = False
        db_handler.save(user_dic)

