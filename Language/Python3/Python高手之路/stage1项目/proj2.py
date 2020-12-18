""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 
工具： python == 3.7.6
介绍： 深度之眼《Python高手之路》项目实战1-2：购物商城
注意： 理清逻辑关系，可以先绘制流程图。善用tag和while true循环进行输入信息的执行和检测。
"""

"""
需求:
    用户名，密码和余额存放于文件中，格式为：Albert|Albert123|3000
    启动程序后：
        已注册用户===>先登录===>登录成功===>读取用户余额===>开始购物
                     登录过程中，用户密码输入超过三次则退出程序,
                     并将用户名添加到黑名单，再次启动程序登陆用户名，提示用户禁止登陆
        未注册用户===>先注册===>注册成功===>输入用户工资，即为用户余额===>开始购物
                     注册过程中，用户密码输入两次一样才可以注册
    允许用户根据商品编号购买商品，比如：
        1 iPhone
        2 macbook
        3 bike
    用户选择商品后，检测余额是否够，够就直接扣款，修改文件中用户余额，不够就提醒
    可随时退出，退出时，打印已购买商品和余额
"""

import os

# 产品列表，分别为品名和单价
product_list = [
    ['IphoneXR', 9800],
    ['Coffee', 30],
    ['Mac Pro 2019', 25000],
    ["Albert's Python Book", 99],
    ['Bike', 199],
    ['ViVo X20', 2499],
]

shopping_cart = {}
current_user_info = []
db_file = r'db.txt' # 数据库信息

while True:
    print('''
    1：Register
    2：Login
    3：Shop
    ''')

    choice = input("""
    Please choose the function by inputting corresponding number, 
    if you input q, you'll quit the program>>:""").strip()

    """
    用户注册模块
    """
    if choice == '1':
        username = input('please input your username>>: ').strip()
        while True: # 验证两次输入密码一致
            password1 = input('please input your password>>: ').strip()
            password2 = input('please verify your password>>: ').strip()
            if password1 == password2:
                print('Register successfully, input 2 to login')
                break
            else:
                print('The twice password are inconsistent. Please input again')

        with open(db_file, 'a', encoding='utf-8') as f: # 将用户信息添加到数据库文件中
            f.write('%s|%s\n' % (username, password1))
            f.flush() # flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入
    
    """
    用户登录模块
    """
    if choice == '2':
        tag = True
        error_count = 0 # 记录登录失败的次数

        while tag:
            if error_count == 3: # 错误3次将退出程序
                print("You've tried too many times. You'll quit the program")
                break
            username = input('username>>:').strip()
            password = input('password>>:').strip()

            # 从数据库中直接读取已有用户信息
            with open(db_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip('\n')
                    user_info = line.split('|') # 解析出当前行的用户数据
                    username_of_db = user_info[0]
                    password_of_db = user_info[1]

                    if username == username_of_db and password == password_of_db:
                        print('Login successfully')

                        # 检测用户账户中是否存在余额
                        if len(user_info) == 3: # 用户账户中第3项保存用户账户余额
                            balance_of_db = user_info[2]
                            balance = int(balance_of_db)
                        else: # 表示用户账户中无余额，此时需要用户输入薪水作为账户余额
                            while True:
                                salary = input('please input your salary>>:').strip()
                                if not salary.isdigit(): # salary必须为数字
                                    continue
                                salary = int(salary)
                                balance = salary
                                break
                        
                        # 将用户余额添加到列表中
                        current_user_info = [username_of_db, balance]
                        print('Hello %s, your balance is %s, input 3 to start shopping' % (
                            current_user_info[0], current_user_info[1]))
                        tag = False # 完成登录，结束登录模块
                        break
                    
                    else: # 密码输入错误
                        print('username or password is invalid')
                        count += 1
    
    """
    用户购物模块
    """
    if choice == '3':
        # 登录或者获取用户的账户信息
        if not current_user_info:
            print('Please login first')
        else:
            username_of_db = current_user_info[0]
            balance = current_user_info[1]
            print('Dear user[%s], your balance is [%s], wish you enjoy your shopping' % (
                username_of_db,
                balance
            ))

            tag = True
            while tag:
                # 选择商品
                for index, product in enumerate(product_list):
                    print(index, product)
                choice = input("Input the numbers of product. if you input q, you'll quit the program>>:").strip()

                if choice.isdigit():
                    choice = int(choice)
                    if choice < 0 or choice >= len(product_list):
                        continue
                    
                    product_name = product_list[choice][0]
                    product_price = product_list[choice][1]

                    # 判断购买力
                    if balance > product_price:
                        if product_name in shopping_cart: # 已经购买过本商品
                            shopping_cart[product_name]['count'] += 1 # 商品数量加一
                        else:
                            shopping_cart[product_name] = {'product_price': product_price, 'count': 1}

                        # 更新余额
                        balance -= product_price
                        current_user_info[1] = balance
                        print("Added product " + product_name + " into shopping cart,your current balance " + str(balance))

                    else:
                        print(
                            "You can't afford the product. The price of the product is %s, and you're lack of %s yuan"
                            % (
                                product_price,
                                product_price - balance
                            ))
                    
                    print('your shopping cart is %s' % shopping_cart)

                # 打印当前所有购物车产品
                elif choice == 'q':
                    print("--------------------------------The goods list you've bought--------------------------------")
                    total_cost = 0
                    for i, key in enumerate(shopping_cart):
                        print('%s%23s%23s%23s%23s' % (
                            i,
                            key,
                            shopping_cart[key]['count'],
                            shopping_cart[key]['product_price'],
                            shopping_cart[key]['product_price'] * shopping_cart[key]['count']
                        ))
                        total_cost += shopping_cart[key]['product_price'] * shopping_cart[key]['count']

                    print("""
                    your total expenditure: %s
                    your balance: %s
                    """ % (total_cost, balance))

                    while tag:
                        inp = input('Confirm purchase(yes/no?)>>: ').strip()
                        if inp not in ['Y', 'N', 'y', 'n', 'yes', 'no']:
                            continue

                        # 确认购买，更新余额信息
                        if inp in ['Y', 'y', 'yes']:
                            src_file = db_file
                            dst_file = r'%s.swap' % db_file

                            with open(src_file, 'r', encoding='utf-8') as read_file, \
                                    open(dst_file, 'w', encoding='utf-8') as write_file:
                                for line in read_file:
                                    if line.startswith(username_of_db):
                                        user_info_line_list = line.strip('\n').split('|')
                                        balance_of_db = balance
                                        balance_of_db = str(balance_of_db)
                                        if len(user_info_line_list) == 2:
                                            user_info_line_list.append(balance_of_db)
                                        else:
                                            user_info_line_list[-1] = balance_of_db
                                        line = '|'.join(user_info_line_list) + '\n'

                                    write_file.write(line)
                            os.remove(src_file)
                            os.rename(dst_file, src_file)

                            print("You've bought successfully. Please wait for the goods patiently")

                        shopping_cart = {}
                        current_user_info = []
                        tag = False

            else:
                    print('Invalid operation')
    elif choice == 'q':
        break

    else:
        print('Invalid operation')



                



                
                




                        




                                

                        
                            
                    

                    
                    



