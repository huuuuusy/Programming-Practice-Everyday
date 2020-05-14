""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 
工具： python == 3.7.6
介绍： 深度之眼《Python高手之路》作业02:流程控制
"""

"""
作业一
写一个用户登录认证的程序，比如用户名是“Albert”，密码是“1”，请用户分别输入用户名和密码来认证
"""

def hw1():
    name = input('please input username:')
    password = input('please input passwword:')
    if name == 'Albert' and password == '1':
        print('Albert login success')
    else:
        print('Error')

"""
作业二
写一个打印用户权限的程序，请用户输入用户名来验证
Albert --> 超级管理员
tom  --> 普通管理员
jack,rain --> 业务主管
其他 --> 普通用户'
"""
def hw2():
    name = input('请输入用户名字：')
    if name == 'Albert':
        print('超级管理员')
    elif name == 'tom':
        print('普通管理员')
    elif name == 'jack' or name == 'rain':
        print('业务主管')
    else:
        print('普通用户')


"""
练习三
写一个根据当日日期来说明是否上班的程序，请用户输入日期来获取
如果:今天是Monday,那么:上班
如果:今天是Tuesday,那么:上班
如果:今天是Wednesday,那么:上班
如果:今天是Thursday,那么:上班
如果:今天是Friday,那么:上班
如果:今天是Saturday,那么:出去浪
如果:今天是Sunday,那么:出去浪
"""
def hw3():
    today = input(">>:")
    if today in ['Saturday', 'Sunday']:
        print('出去浪')
    elif today in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        print('上班')
    else:
        print('''必须输入其中一种:
        Monday
        Tuesday
        Wednesday
        Thursday
        Friday
        Saturday
        Sunday
        ''')

"""
练习四
写一个循环验证用户登录的程序，用户认证登录成功后，输入“q”退出程序，用户认证失败后重复让用户执行登录操作，当用户重复次数超过3次仍没有登录成功，则退出程序。
"""
def hw4():
    username = 'albert'
    password = '1'
    count = 0
    tag = True
    while tag:
        username_input = input('username>>:').strip()
        password_input = input('password>>:').strip()
        if count == 3:
            break
        if username_input == username and password_input == password:
            print('success')
            while tag:
                cmd = input('>>:').strip()
                if cmd == 'q':
                    tag = False
                    break
        else:
            print('usename or password is error')
            count += 1

"""
练习五
写一个用户猜年龄的游戏，允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序，如何猜对了，就直接退出。
"""
def hw5():
    Albert_age = 18
    count = 0
    while True:
        if count == 3:
            choice = input('继续(Y/N?)>>: ')
            if choice == 'Y' or choice == 'y':
                count = 0
            else:
                break
        guess = int(input('>>: '))
        if guess == Albert_age:
            print('you win')
            break
        else:
            print('guess again')
        count += 1


"""
练习六
按要求打印如下结果：
1. 使用while循环输出1 2 3 4 5 6 8 9 10
2. 求1-100的所有数的和
3. 输出 1-100 内的所有奇数
4. 输出 1-100 内的所有偶数
5. 求1-2+3-4+5 ... 99的所有数的和
"""
def hw6():
    print('ex1:')
    for i in range(1,11):
        if i != 7:
            print(i,end=' ') # 在print中使用end指定每个字符之间的间隔符号
    print()

    print('ex2:')
    sum = 0
    for i in range(1,101):
        sum += i
    print(sum)

    print('ex3:')
    for i in range(1,101):
        if i%2 != 0:
            print(i,end=' ')
    print()
    
    print('ex4:')
    for i in range(1,101):
        if i%2 == 0:
            print(i,end=' ')
    print()
    
    print('ex5:')
    sum = 0
    for i in range(1,101):
        if i%2 != 0:
            sum += i
        else:
            sum -= i
    print(sum)


"""
练习七
打印如下金字塔图形，下图为等腰三角形，上面一行内容永远比下面少两颗星星且位于下面一行的正上（提示：用两层for loop）
    *
   ***
  *****
 *******
*********
分析
#max_level=5
    *        #current_level=1,空格数=4,*号数=1
   ***       #current_level=2,空格数=3,*号数=3
  *****      #current_level=3,空格数=2,*号数=5
 *******     #current_level=4,空格数=1,*号数=7
*********    #current_level=5,空格数=0,*号数=9
#数学表达式
空格数=max_level-current_level
*号数=2*current_level-1
"""
def hw7():
    max_level = 5
    for current_level in range(1,max_level+1):
        for i in range(max_level - current_level):
            print(' ',end='')
        for j in range(2*current_level-1):
            print('*',end='')
        print()

if __name__ == "__main__":
    #hw1()
    #hw2()
    #hw3()
    #hw4()
    #hw5()
    #hw6()
    hw7()