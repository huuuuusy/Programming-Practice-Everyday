""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code
工具： python3
"""

"""
实验2-2:温度转换
"""
fahrenheit = 0
print("Fahrenheit Celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8 # 转换为摄氏度
    print("{:5d} {:7.2f}".format(fahrenheit , celsius))
    fahrenheit = fahrenheit + 25