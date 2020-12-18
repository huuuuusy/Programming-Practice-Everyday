""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路：
    倒序检索，然后用pop弹出不符合要求的重复元素
结果：
    执行用时 : 76 ms, 在所有 Python3 提交中击败了41.34%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.08%的用户
"""

class Solution(object):
    def removeDuplicates(self, nums):
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1] and nums[i-1] == nums[i-2] and i-2 >= 0: 
                nums.pop(i)
        return len(nums)

if __name__ == "__main__":
    nums = [1,1]
    answer = Solution().removeDuplicates(nums)
    print(answer)