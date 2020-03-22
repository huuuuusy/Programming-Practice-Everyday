""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.39
工具： python == 3.7.3
"""

"""
思路:
    动态规划
结果：
    执行用时 : 64 ms, 在所有 Python3 提交中击败了76.50%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.19%的用户
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid or not obstacleGrid[0]: return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0]*col for _ in range(row)]
        # 首位置
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        if dp[0][0] == 0: return 0 # 如果出发点有障碍物，则没有道路
        # 第一行
        for j in range(1, col):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = dp[0][j-1]
        # 第一列
        for i in range(1, row):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

if __name__ == "__main__":
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    answer = Solution().uniquePathsWithObstacles(obstacleGrid)
    print(answer)