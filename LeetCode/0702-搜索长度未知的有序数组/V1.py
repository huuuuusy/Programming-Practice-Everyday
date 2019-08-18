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
    执行用时 : 56 ms, 在所有 Python3 提交中击败了100%的用户
    内存消耗 : 14.6 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # 按照数组最大的可能性设置左右边界
        left = 0
        right = 20000
        while left < right:
            mid = (left + right + 1) >> 1 # 右中位数
            if reader.get(mid) == 2147483647: # 如果越界，则右边界收缩
                right = mid - 1
            elif reader.get(mid) > target: # 如果大于目标值，则右边界收缩
                right = mid - 1
            else:
                left = mid
        return left if reader.get(left) == target else -1 # 返回结果
            
        