""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

任务：
让用户输入一个数字，并指出这个数字是否是10的整数倍
"""

number = input("Give me a number, please: ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")