""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code
工具： python3
"""

"""
计算出一个半径为 2 的圆的面积，并且把面积打印出来，保留小数点后 10 位。

不要使用 input 等方法获得输入，程序不需要输入任何参数，直接输出半径为 2 的圆的面积
"""

import math
# 计算圆的面积
area = 2 * 2 * math.pi
# 格式化输出圆的面积，保留10位小数
print("{:.10f}".format(area))
