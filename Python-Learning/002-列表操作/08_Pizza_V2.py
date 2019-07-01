""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

任务：在07_Pizza中，创建比萨列表的副本，并将其存储到变量friend_pizzas中
1. 在原来的比萨列表中添加一种比萨
2. 在列表friend_pizzas中添加另一种比萨
3. 核实你有两个不同的列表
为此，打印消息My favorite pizzas are:再使用一个for循环打印第一个列表；
打印消息My friend’s favorite pizzas are:再使用一个for循环打印第二个列表;
核实新增的比萨被添加到正确的列表中
"""

favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("meat lover's")
friend_pizzas.append('pesto')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)