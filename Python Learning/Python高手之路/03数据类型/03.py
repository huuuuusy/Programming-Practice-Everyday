""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 
工具： python == 3.7.6
介绍： 深度之眼《Python高手之路》作业03：数据类型
"""

"""
作业一
写代码,有如下变量,请按照要求实现每个功能
"""

def hw1():
    name = " alberT"
    print(name)
    print('移除 name 变量对应的值两边的空格,并输出处理结果: ',end='')
    print(name.strip())
    print()

    print('判断 name 变量对应的值是否以 "al" 开头,并输出结果: ',end='')
    print(name.startswith('al'))
    print()

    print('判断 name 变量对应的值是否以 "T" 结尾,并输出结果: ',end='')
    print(name.endswith('T'))
    print()
    
    print('将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果: ',end='')
    print(name.replace('l', 'p'))
    print()

    print('将 name 变量对应的值根据 “l” 分割,并输出结果: ',end='')
    print(name.split('l'))
    print()

    print('将 name 变量对应的值变大写,并输出结果: ',end='')
    print(name.capitalize())
    print()

    print('将 name 变量对应的值变小写,并输出结果: ',end='')
    print(name.lower())
    print()

    print('请输出 name 变量对应的值的第 2 个字符: ',end='')
    print(name[2])
    print()

    print('请输出 name 变量对应的值的前 3 个字符: ',end='')
    print(name[:3])
    print()

    print('请输出 name 变量对应的值的后 2 个字符: ',end='')
    print(name[-2:])
    print()

    print('请输出 name 变量对应的值中 “e” 所在索引位置: ',end='')
    print(name.index('e'))
    print()

    print('获取子序列,去掉最后一个字符。如: albert 则获取 alber: ',end='')
    print(name[:-1])
    print()

"""
作业二
有列表data=['albert',18,[2000,1,1]]，分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量。
"""

def hw2():
    data=['albert',18,[2000,1,1]]
    name = data[0]
    age = data[1]
    birthday = data[2]
    year = birthday[0]
    month = birthday[1]
    day = birthday[2]
    print(name, age, birthday, year, month, day)

"""
作业三
有如下值集合 [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中，即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
"""
def hw3():
    a = {'k1': [], 'k2': []}
    c = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
    for i in c:
        if i > 66:
            a['k1'].append(i)
        elif i < 66:
            a['k2'].append(i)
    print(a)


"""
作业四
1. 列表l=['a','b',1,'a','a']，列表元素均为可不可变类型，去重得到新列表,且新列表无需保持列表原来的顺序
2. 在上题的基础上，保存列表原来的顺序
3. 有如下列表，列表元素为可变类型，去重，得到新列表，且新列表一定要保持列表原来的顺序
l = [
    {'name': 'albert', 'age': 18, 'sex': 'male'},
    {'name': 'james', 'age': 35, 'sex': 'male'},
    {'name': 'taylor', 'age': 25, 'sex': 'female'},
    {'name': 'albert', 'age': 18, 'sex': 'male'},
    {'name': 'albert', 'age': 18, 'sex': 'male'},
]
"""
def hw4():
    print('ex1:')
    l=['a','b',1,'a','a']
    print(set(l))

    print('ex2:')
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    print(res)      

    print('ex3:') 
    l = [
    {'name': 'albert', 'age': 18, 'sex': 'male'},
    {'name': 'james', 'age': 35, 'sex': 'male'},
    {'name': 'taylor', 'age': 25, 'sex': 'female'},
    {'name': 'albert', 'age': 18, 'sex': 'male'},
    {'name': 'albert', 'age': 18, 'sex': 'male'},
    ]
    s = set()
    res = []
    for info in l:
        val = (info['name'], info['age'], info['sex'])
        if val not in s:
            s.add(val) # 注意集合中元素添加使用add()
            res.append(info)
    print(res)

"""
作业五
使用至少两种方法统计字符串 s='hello albert albert say hello world world'中每个单词的个数，结果如：
{'hello': 2, 'albert': 2, 'say': 1, 'world': 2}
"""
def hw5():
    s='hello albert albert say hello world world'
    print('method 1:')
    d1 = {}
    words = s.split()
    for word in words:
        d1[word] = s.count(word)
    print(d1)
    
    print('method 2:')
    d2 = {}
    words = s.split()
    for word in words:
        d2.setdefault(word, s.count(word))
    print(d2)

"""
实现简易购物程序,要求如下：首先打印商品详细信息，然后请用户输入商品名和购买个数，则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入
msg_dic = {
    'apple': 10,
    'tesla': 1000000,
    'mac': 10000,
    'iphone': 8000,
    'chicken': 30,
    'pen': 3,
    'ruler': 5
}
"""
def hw6():
    msg_dic = {
    'apple': 10,
    'tesla': 1000000,
    'mac': 10000,
    'iphone': 8000,
    'chicken': 30,
    'pen': 3,
    'ruler': 5
    }
    shop_list = []
    while True:
        # 打印购物清单
        for product, price in msg_dic.items():
            print('product: %s, price: %s' % (product, price))
        choice = input('please input product name>>: ').strip()
        # 选择产品名称
        if choice == 'q':
            break
        elif choice not in msg_dic:
            print('Invalid input, please input again!')
            continue
        else:
            # 选择产品数量
            while True:
                count = input('please input the number of product>>: ').strip()
                if not count.isdigit():
                    print('Invalid input, please input again!')
                    continue
                else:
                    shop_list.append((choice, msg_dic[choice], count))    
                    print(shop_list)
                    break
                    
if __name__ == "__main__":
    #hw1()
    #hw2()
    #hw3()
    #hw4()
    #hw5()
    hw6()