""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

任务：利用列表生成数字
"""

"""
创建一个列表，其中包含3~30能被3整除的数
再使用一个for循环将这个列表中的数字都打印出来
"""

numbers = list(range(3, 31, 3))
for number in numbers:
    print(number)

"""
创建一个列表，其中包含前10个整数（即1～10）的立方
再使用一个for循环将这些立方数都打印出来
"""

cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

"""
使用列表解析生成一个列表，其中包含前10个整数的立方
"""

cubes = [number**3 for number in range(1, 11)]

for cube in cubes:
    print(cube)

