""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37.1
工具： python == 3.7.3
"""

"""
思路:
    list＋str转换类型法
结果：
    执行用时 : 56 ms, 在所有 Python3 提交中击败了44.91%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.54%的用户
"""

class Solution:
    def addDigits(self, num):
        while num > 9:
            num = sum([int(num) for num in list(str(num))])
        return num

if __name__ == "__main__":
    num = 38
    answer = Solution().addDigits(num)
    print(answer)


