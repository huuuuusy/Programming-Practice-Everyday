""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code
工具： python3
"""

"""
实验5-3:打印 10 以内的乘法表
"""
#!/usr/bin/env python3
i = 1
print("-" * 50)
while i < 11:
    n = 1
    while n <= 10:
        print("{:5d}".format(i * n), end=' ')
        n += 1
    print()
    i += 1
print("-" * 50)