""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code
工具： python3
"""

"""
实验5-4:用户输入一个整数，如果输入的是负数，那么我们会再次要求输入，如果输入的是整数，我们计算这个数的平方。用户输入 0 来跳出这个无限循环。
"""
#!/usr/bin/env python3
while True:
    n = int(input("Please enter an Integer: "))
    if n < 0:
        continue # 这会返回到循环开始处执行
    elif n == 0:
        break
    print("Square is ", n ** 2)
print("Goodbye")