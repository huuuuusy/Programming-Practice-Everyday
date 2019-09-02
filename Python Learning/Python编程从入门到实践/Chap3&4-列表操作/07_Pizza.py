""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
任务： 想出至少三种喜欢的比萨，将其名称存储在一个列表中，再使用for循环将每种比萨的名称都打印出来
        1. 修改这个for循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称
        2. 在程序末尾添加一行代码，它不在for循环中，指出你有多喜欢比萨
"""

favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']

# 打印所有pizza的名称
for pizza in favorite_pizzas:
    print(pizza)

print("\n")

# 针对每种pizza打印句子
for pizza in favorite_pizzas:
    print("I really love " + pizza + " pizza!")

print("\nI really love pizza!")