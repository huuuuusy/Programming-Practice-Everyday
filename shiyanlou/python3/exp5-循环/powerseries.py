""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code
工具： python3
"""

"""
实验5-2:幂级数,e^x = 1 + x + x^2 / 2! + x^3 / 3! + ... + x^n / n! （0 < x < 1）
"""
#!/usr/bin/env python3
x = float(input("Enter the value of x: "))
n = term = num = 1
result = 1.0
while n <= 100:
    term *= x / n
    result += term
    n += 1
    if term < 0.0001:
        break
print("No of Times= {} and Sum= {}".format(n, result))