from db import db_handler
from lib import common

bank_logger = common.get_logger('bank')


def check_balance_interface(name):
    user_dic = db_handler.select(name)
    return user_dic['balance']


def transfer_interface(from_name, to_name, balance):
    if from_name == to_name:
        return False, '不能给自己转钱'
    to_dic = db_handler.select(to_name)
    if to_dic:
        from_dic = db_handler.select(from_name)
        if from_dic['balance'] >= balance:
            to_dic['balance'] += balance
            from_dic['balance'] -= balance
            from_dic['bankflow'].append('您向 %s 转账 %s 元' % (to_name, balance))
            to_dic['bankflow'].append('您收到%s 转账 %s 元' % (from_name, balance))
            db_handler.save(from_dic)
            db_handler.save(to_dic)
            bank_logger.info('您收到%s 转账 %s 元' % (from_name, balance))
            return True, '转账成功'
        else:
            return False, '你钱不够'


    else:
        return False, '您要转账的人不存在'


def repay_interface(name, balance):
    user_dic = db_handler.select(name)
    user_dic['balance'] += balance
    user_dic['bankflow'].append('您还款 %s 元' % balance)
    db_handler.save(user_dic)
    bank_logger.info('您还款%s元' % balance)
    return True, '还款成功'


def withdraw_interface(name, balance):
    user_dic = db_handler.select(name)
    balance1 = balance * 1.05
    if user_dic['balance'] >= balance1:
        user_dic['balance'] -= balance1
        user_dic['bankflow'].append('您取款 %s 元' % balance)
        db_handler.save(user_dic)
        return True, '取款成功'
    else:
        return False, '余额不足'


def check_record_interface(name):
    user_dic = db_handler.select(name)
    return user_dic['bankflow']


def consume_interface(name, cost):
    user_dic = db_handler.select(name)
    if user_dic['balance'] >= cost:
        user_dic['balance'] -= cost
        db_handler.save(user_dic)
        return True, '扣款成功'
    else:
        return False, '余额不足'
