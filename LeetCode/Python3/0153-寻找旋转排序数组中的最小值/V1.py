""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    nums[mid] > nums[right]：
        例子：[7, 8, 9, 10, 1, 2]，mid 肯定不是最小
    nums[mid] < nums[right]：
        例子：[8, 9, 1, 2, 3, 4, 5, 6]，此时 mid 有可能是最小
参考：
    https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/er-fen-fa-fen-zhi-fa-python-dai-ma-java-dai-ma-by-/
结果：
    执行用时 : 60 ms, 在所有 Python3 提交中击败了49.12%的用户
    内存消耗 : 13.6 MB, 在所有 Python3 提交中击败了5.08%的用户
"""

class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums)-1 
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1 # 左边界收缩
            else:
                right = mid
        return nums[left]

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    answer = Solution().findMin(nums)
    print(answer)