from db import db_handler
from interface import bank


def check_shoppingcart(name):
    user_dic = db_handler.select(name)
    return user_dic['shoppingcart']


def shopping_interface(name, cost, shoppingcart):
    flg, msg = bank.consume_interface(name, cost)
    if flg:
        user_dic = db_handler.select(name)
        user_dic['shoppingcart'] = shoppingcart
        db_handler.save(user_dic)
        return True, '购买成功'
    else:
        return False, msg
