""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    dp[i] = min(dp[i] + dp[i - 1], dp[i] + dp[i - 2])
结果：
    执行用时 : 80 ms, 在所有 Python3 提交中击败了75.38%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了5.26%的用户
"""

class Solution:
    def minCostClimbingStairs(self, cost):
        # 先存储前两个花销
        f = [cost[0], cost[1]]
        # 动态规划，添加每次爬楼梯最小的代价
        for i in range(2, len(cost)):
            f.append(cost[i]+min(f[i-1], f[i-2]))
        return min(f[-1], f[-2])
 
if __name__ == "__main__":
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    answer = Solution().minCostClimbingStairs(cost)
    print(answer)