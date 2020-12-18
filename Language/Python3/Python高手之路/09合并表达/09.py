""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 
工具： python == 3.7.6
介绍： 深度之眼《Python高手之路》作业09：合并表达
"""

"""
练习1：
将names=['albert','james','kobe','kd']中的名字全部变大写
"""
def hw1():
    names=['albert','james','kobe','kd']
    names_list = list(map(lambda x: x.capitalize(), names))
    print(names_list)

"""
练习2：
将names=['albert','jr_shenjing','kobe','kd']中以shenjing结尾的名字过滤掉，然后保存剩下的名字长度
"""
def hw2():
    names = ['albert', 'jr_shenjing', 'kobe', 'kd']
    names_list = list(filter(lambda x: not x.endswith('shenjing'), names))
    print(names_list)
    new_names_list = list(map(lambda x:len(x), names_list))
    print(new_names_list)

"""
练习3：
求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）
"""
def hw3():
    with open('a.txt', mode='r', encoding='utf-8') as f:
        max_len = len(max([line.strip() for line in f], key = lambda x:len(x)))
        print(max_len)

"""
练习4：
文件shopping.txt内容如下，分别代表商品，价格和数量
mac,20000,3
lenovo,3000,10
bmw,1000000,10
chicken,200,1
（1）求总共花了多少钱？
（2）打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]
（3）求单价大于10000的商品信息,格式同上
"""
def hw4():
    with open('shopping.txt', mode='r', encoding='utf-8') as f:
        info = [line.strip().split(',') for line in f]
        cost = sum(float(unit_price) * int(count) for _, unit_price, count in info)
        print(cost)

    with open('shopping.txt', mode='r', encoding='utf-8') as f:
        info = [{
            'name': line.strip().split(',')[0],
            'price': float(line.strip().split(',')[1]),
            'count': int(line.strip().split(',')[2]),
        } for line in f]
        print(info)
    
    with open('shopping.txt', mode='r', encoding='utf-8') as f:
        info = [{
            'name': line.strip().split(',')[0],
            'price': float(line.strip().split(',')[1]),
            'count': int(line.strip().split(',')[2]),
        } for line in f if float(line.strip().split(',')[1]) > 10000]
        print(info)
    


if __name__ == '__main__':
    #hw1()
    #hw2()
    #hw3()
    hw4()

