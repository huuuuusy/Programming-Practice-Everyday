""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
"""

"""
思路:
    动态规划，和V1的暴力解法思路基本相同
    分类讨论的标准是：若之前的和小于 0，则将最大和置为当前值，否则计算最大和
    1、定义状态：dp[i] 表示以 nums[i] 结尾的连续子数组的最大和
    2、状态转移方程：dp[i] = max{num[i], dp[i - 1] + num[i]}
结果：
    执行用时 : 56 ms, 在所有 Python 提交中击败了91.27%的用户
    内存消耗 : 13.9 MB, 在所有 Python 提交中击败了22.44%的用户
"""

class Solution:
    def maxSubArray(self, nums):
        # 先单独列出两种特殊情况
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # dp是和原始数列等长的列表，初始化时全部元素为0
        # dp[i]表示以nums[i]结尾的连续子数组的最大和
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            # 状态转移方程
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)

if __name__ == "__main__":
    nums =  [-2,1]
    answer = Solution().maxSubArray(nums)
    print(answer)
        