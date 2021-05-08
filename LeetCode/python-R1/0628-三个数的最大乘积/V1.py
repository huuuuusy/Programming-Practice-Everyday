""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.39
工具： python == 3.7.3
"""

"""
思路:
    注意考虑负数的情况
    最大乘积要么为三个正数，要么为两负一正
结果：
    执行用时 : 492 ms, 在所有 Python3 提交中击败了24.22%的用户
    内存消耗 : 14.8 MB, 在所有 Python3 提交中击败了5.14%的用户
"""

class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])

if __name__ == "__main__":
    nums = [1,2,3,4]
    answer = Solution().maximumProduct(nums)
    print(answer)