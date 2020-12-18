""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路：
    直接计算
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了91.03%的用户
    内存消耗 : 13.3 MB, 在所有 Python3 提交中击败了47.28%的用户
"""

class Solution:
    def reverse(self, x):
        if x != 0:
            y = int(str(abs(x))[::-1]) * (x // abs(x))
            if y >= -2 ** 31 and y <= 2 ** 31 - 1:
                return y
        return 0

if __name__ == "__main__":
    num = 1534236469
    answer = Solution().reverse(num)
    print(answer)
