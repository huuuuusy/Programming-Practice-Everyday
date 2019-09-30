""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    动态规划
结果：
    执行用时 : 36 ms, 在所有 Python3 提交中击败了98.50%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了5.14.00%的用户
"""

class Solution:
    def uniquePaths(self, m, n):
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)] # 注意，对于第一行 dp[0][j]，或者第一列 dp[i][0]，由于都是在边界，所以只能为 1
        # 动态方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
        return dp[-1][-1]

if __name__ == "__main__":
    m = 3
    n = 2
    answer = Solution().uniquePaths(m, n)
    print(answer)