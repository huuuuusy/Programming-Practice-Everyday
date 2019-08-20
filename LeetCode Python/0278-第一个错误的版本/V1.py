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
    执行用时 : 20 ms, 在所有 Python3 提交中击败了78.40%的用户
    内存消耗 : 11.7 MB, 在所有 Python3 提交中击败了26.29%的用户
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1 
        right = n 
        while left < right:
            mid = (left + right) >> 1 # 左中位数
            if isBadVersion(mid) == False:
                left = mid + 1 # 左边界收缩
            else:
                right = mid 
        return left