""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    对k的特殊取值进行处理，然后切片
结果：
    执行用时 : 72 ms, 在所有 Python3 提交中击败了77.16%的用户
    内存消耗 : 13.2 MB, 在所有 Python3 提交中击败了97.14%的用户
"""

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if k != 0:
            if k > len(nums):
                k -= len(nums)
            nums[:k],nums[k:] = nums[-k:],nums[:-k]
        return nums

if __name__ == "__main__":
    k = 8
    nums = [1,2,3,4,5,6,7]
    answer = Solution().rotate(nums,k)
    print(answer)