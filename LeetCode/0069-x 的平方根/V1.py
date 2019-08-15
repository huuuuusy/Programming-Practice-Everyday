""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    二分查找，右中位数，右边界收缩
结果：
    执行用时 : 92 ms, 在所有 Python3 提交中击败了14.67%的用户
    内存消耗 : 14 MB, 在所有 Python3 提交中击败了5.22%的用户
"""

class Solution:
    def mySqrt(self, x):
        left = 0
        right = x // 2 + 1 
        # 固定写法,left < right
        while left < right:
            mid = (left + right + 1) >> 1  # 右中位数
            square = mid * mid 
            if square > x:
                right = mid - 1 # 右边界收缩
            else:
                left = mid
        # return left或者right都可以
        return right

if __name__ == "__main__":
    x = 4
    answer = Solution().mySqrt(x)
    print(answer)