""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    利用双指针，分别正查倒查确定指针位置并返回
结果：
    执行用时 : 300 ms, 在所有 Python3 提交中击败了67.87%的用户
    内存消耗 : 15 MB, 在所有 Python3 提交中击败了5.67%的用户
"""

class Solution:
    def findUnsortedSubarray(self, nums):
        new_nums = sorted(nums)
        left = 0 
        right = 0
        for i in range(len(nums)):
            if nums[i] != new_nums[i]:
                left = i
                break
        for i in range(len(nums),0,-1):
            if nums[i-1] != new_nums[i-1]:
                right = i-1 
                break
        return 0 if left == right else right-left+1

if __name__ == "__main__":
    nums = [1,2,3,4]
    answer = Solution().findUnsortedSubarray(nums)
    print(answer)