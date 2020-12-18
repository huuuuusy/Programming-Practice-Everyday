""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    直接解题
结果：
    执行用时 : 108 ms, 在所有 Python3 提交中击败了30.40%的用户
    内存消耗 : 16.1 MB, 在所有 Python3 提交中击败了11.43%的用户
"""

class Solution:
    def findDuplicate(self, nums):
        new_nums = sorted(nums)
        for i in range(len(new_nums)):
            if new_nums[i] == new_nums[i+1]:
                return new_nums[i]
            else:
                continue

if __name__ == "__main__":
    nums = [1,3,4,2,2]
    answer = Solution().findDuplicate(nums)
    print(answer)
        