from interface import user, bank, shopping
from lib import common

user_data = {
    'name': None
}


def logout():
    user_data['name'] = None


def login():
    print('登陆')
    if user_data['name']:
        print('您已经登陆了')
        return
    count = 0
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':break
        password = input('请输入密码：').strip()
        flag, msg = user.login_interface(name, password)
        if flag:
            user_data['name'] = name
            print(msg)
            break
        else:
            print(msg)
            count += 1
            if count == 3:
                user.lock_user_interface(name)
                print('尝试过多，锁定')
                break


def register():
    print('注册')
    if user_data['name']:
        print('您已经登陆了')
        return
    while True:
        name = input('请输入名字:').strip()
        if name == 'q': break
        password = input('请输入密码').strip()
        conf_password = input('请确认密码').strip()
        if password == conf_password:
            flag, msg = user.register_interface(name, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


@common.login_auth
def check_balance():
    print('查看余额')
    balance = bank.check_balance_interface(user_data['name'])
    print(balance)


@common.login_auth
def transfer():
    print('转账')
    while True:
        to_name = input('请输入转给的账号：').strip()
        balance = input('请输入转账金额:').strip()
        if balance.isdigit():
            balance = int(balance)
            flag, msg = bank.transfer_interface(user_data['name'], to_name, balance)
            if flag:
                print(msg)
                break
            else:
                print(msg)


@common.login_auth
def repay():
    print('还款')
    balance = input('请输入还款金额:').strip()
    if balance.isdigit():
        balance = int(balance)
        flg, msg = bank.repay_interface(user_data['name'], balance)
        if flg:
            print(msg)
        else:
            print(msg)
    else:
        print('必须输入数字')


@common.login_auth
def withdraw():
    print('取款')
    balance = input('请输入取款金额：').strip()
    if balance.isdigit():
        balance = int(balance)
        flag, msg = bank.withdraw_interface(user_data['name'], balance)
        if flag:
            print(msg)
        else:
            print(msg)


@common.login_auth
def check_record():
    print('查看流水')
    bankflow = bank.check_record_interface(user_data['name'])
    for flow in bankflow:
        print(flow)


@common.login_auth
def shop():
    '''
    1 先循环打印出商品
    2 用户输入数字选择商品（判断是否是数字，判断输入的数字是否在范围内）
    3 取出商品名，商品价格
    4 判断用户余额是否大于商品价格
    5 余额大于商品价格时，判断此商品是否在购物车里
        5.1 在购物车里，个数加1
        5.1 不在购物车里，拼出字典放入（｛‘good’：｛‘price’：10，‘count’：1｝｝）
    6 用户余额减掉商品价格
    7 花费加上商品价格
    8 当输入 q时，购买商品
        8.1 消费为0 ，直接退出
        8.2 打印购物车
        8.3 接受用户输入，是否购买 当输入y，直接调购物接口实现购物
    :return:
    '''
    print('购物')
    goods_list = [
        ['coffee', 10],
        ['chicken', 20],
        ['iphone', 8000],
        ['macPro', 15000],
        ['car', 100000]
    ]
    shoppingcart = {}
    # ｛‘coffee’：｛‘price’：10，‘count’：2｝,‘car’：｛‘price’：10000，‘count’：1｝｝
    cost = 0
    user_balance = bank.check_balance_interface(user_data['name'])
    while True:
        for i, good in enumerate(goods_list):
            print('%s : %s ' % (i, good))
        choice = input('请输入要购买的商品(数字)(q退出并购买)：').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >= len(goods_list): continue
            good_name = goods_list[choice][0]
            good_price = goods_list[choice][1]
            if user_balance >= good_price:
                if good_name in shoppingcart:
                    shoppingcart[good_name]['count'] += 1
                else:
                    shoppingcart[good_name] = {'price': good_price, 'count': 1}
                user_balance -= good_price
                cost += good_price
            else:
                print('余额不足')
        elif choice == 'q':
            if cost == 0: break
            print(shoppingcart)
            buy = input('确认购买吗？（y/n）').strip()
            if buy == 'y':
                flg, msg = shopping.shopping_interface(user_data['name'], cost, shoppingcart)
                if flg:
                    print(msg)
                    break
                else:
                    print(msg)

            else:
                print('您没买东西')
                break
        else:
            print('输入非法')


@common.login_auth
def check_shopping_cart():
    print('查看购物车')
    shoppingcart = shopping.check_shoppingcart(user_data['name'])
    print(shoppingcart)


func_dic = {
    '1': login,
    '2': register,
    '3': check_balance,
    '4': transfer,
    '5': repay,
    '6': withdraw,
    '7': check_record,
    '8': shop,
    '9': check_shopping_cart,
    '10': logout
}


def run():
    while True:
        print('''
        1、登录
        2、注册
        3、查看余额
        4、转账
        5、还款
        6、取款
        7、查看流水
        8、购物
        9、查看购买商品
        10、退出登陆
        ''')
        choice = input('请选择:').strip()
        if choice in func_dic:
            func_dic[choice]()
