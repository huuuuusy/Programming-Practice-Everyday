""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 
工具： python == 3.7.6
介绍： 深度之眼《Python高手之路》作业10：模块对象
"""

"""
练习1：
文件内容如下,标题为:姓名,性别,年纪,薪资
albert male 18 3000
james male 38 30000
林志玲 female 28 20000
新垣结衣 female 28 10000
要求从文件中取出每一条记录放入列表中,列表的每个元素都是如下格式：
{'name':'albert','sex':'male','age':18,'salary':3000}
"""
def hw1():
    list_info = []
    f = open('info.txt', mode='r', encoding='utf-8')
    for line in f:
        data_info = line.split(' ')
        name = data_info[0]
        sex = data_info[1]
        age = data_info[2]
        salary = data_info[3]
        people = {
            'name':name,
            'sex':sex,
            'age':age,
            'salary':salary,
        } 
        list_info.append(people)
    f.close()
    print(list_info)
    return list_info

"""
练习2：
根据题目1得到的列表,取出薪资最高的人的信息
"""
def hw2(list_info):
    info = max(list_info, key=lambda x:x['salary'])
    print(info)

"""
练习3：
根据题目1得到的列表,取出最年轻的人的信息
"""
def hw3(list_info):
    info = min(list_info, key=lambda x:x['age'])
    print(info)

"""
练习4：
根据题目1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
"""
def hw4(list_info):
    info = map(lambda x:x['name'].capitalize(), list_info)
    print(list(info))

"""
练习5：
根据题目1得到的列表,过滤掉名字以a开头的人的信息
"""
def hw5(list_info):
    info = filter(lambda x:not x['name'].startswith('a'), list_info)
    print(list(info))

"""
练习6：
使用递归打印斐波那契数列(前两个数的和得到第三个数，如：0、 1、1、2、3、5、8、13、21...)
"""
def hw6():
    def Fibonacci(n):
        if n < 1:
            return
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return Fibonacci(n-1) + Fibonacci(n-2)
    
    for i in range(1, 20):
        print(Fibonacci(i))

"""
练习7：
使用random模块写一个随机生成8位验证码的程序，验证码中有随机大小写字母和数字
"""
import random
def hw7():
    verification_code = ""
    for i in range(8):
        alpha1 = chr(random.randint(65,90))
        alpha2 = chr(random.randint(97,122))
        number = random.randint(0,9)
        verification_code += random.choice([alpha1, alpha2, str(number)])
    print(verification_code)

if __name__ == '__main__':
    #list_info = hw1()
    #hw2(list_info)
    #hw3(list_info)
    #hw4(list_info)
    #hw5(list_info)
    #hw6()
    hw7()
