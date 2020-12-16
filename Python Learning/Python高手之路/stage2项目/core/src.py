""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 
工具： python == 3.7.6
介绍： 深度之眼《Python高手之路》项目实战2：电子商城
"""

# src.py为核心逻辑文件
from interface import user

# 原始用户信息
user_data = {
    'name': None
}


# 登录
def login():
    print('登录')
    if user_data['name']:
        print('已经登录')
        return
    count = 0 # 统计登录失败次数
    while True:
        name = input('请输入名字').strip()
        if name == 'q':
            break
        password = input('请输入密码').strip()
        flag, msg = user.login_interface(name, password)
        if flag: # 如果登录成功
            user_data['name'] = name
            print(msg)
            break
        else:
            print(msg)
            count += 1
            if count == 3: # 失败三次则锁定用户
                user.lock_user_interface(name)
                print('尝试过多，锁定用户')
                break



# 菜单
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

# 主程序
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
        