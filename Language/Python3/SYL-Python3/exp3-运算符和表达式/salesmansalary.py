""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code
工具： python3
"""

"""
实验3-4:计算一位数码相机销售人员的工资。他的基本工资是 1500，每售出一台相机他可以得到 200 并且获得 2% 的抽成。程序要求输入相机数量及单价。
"""
#!/usr/bin/env python3
basic_salary = 1500
bonus_rate = 200
commission_rate = 0.02
numberofcamera = int(input("Enter the number of inputs sold: "))
price = float(input("Enter the price of camera: "))
bonus = (bonus_rate * numberofcamera)
commission = (commission_rate * price * numberofcamera)
print("Bonus        = {:6.2f}".format(bonus))
print("Commission   = {:6.2f}".format(commission))
print("Gross salary = {:6.2f}".format(basic_salary + bonus + commission))