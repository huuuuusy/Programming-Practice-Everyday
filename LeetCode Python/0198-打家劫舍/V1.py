""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    dp问题, dp[i] = max(dp[i-1], dp[i-2] + nums[i])
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败59.91%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.14%的用户
"""

class Solution:
    def rob(self, nums):
        # 计算特殊情况
        if nums == []:
            return 0 
        if len(nums) <= 2:
            return max(nums)
        dp = [0]*(len(nums))
        dp[0] = nums[0] # 只有一个房子时
        dp[1] = max(dp[0],nums[1])　# 有两个房子时
        # 有多个房子时
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

if __name__ == "__main__":
    nums = [2,7,9,3,1]
    answer = Solution().rob(nums)
    print(answer)