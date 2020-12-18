""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    二分查找
结果：
    执行用时 : 32 ms, 在所有 Python3 提交中击败了14.41%的用户
    内存消耗 : 11.7 MB, 在所有 Python3 提交中击败了37.41%的用户
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n 
        while left < right:
            mid = (left + right) >> 1 # 左中位数
            if guess(mid) == 1:
                left = mid + 1 # 左边界收缩
            else:
                right = mid
        return left
            
