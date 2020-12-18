""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code
工具： python3
"""

"""
实验5-1:斐波那契（Fibonacci）数列
"""
#!/usr/bin/env python3
a, b = 0, 1
while b < 100:
    print(b, end=' ')
    a, b = b, a + b
print()