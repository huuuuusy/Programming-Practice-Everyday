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
    执行用时 : 56 ms, 在所有 Python3 提交中击败了48.02%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.54%的用户
"""


class Solution:
    def fib(self, N):
        dp = [0,1,1]
        if N <= 2:
            return dp[N]
        for i in range(2, N+1):
            dp.append(dp[i] + dp[i-1])
        return dp[N]

if __name__ == "__main__":
    N = 4
    answer = Solution().fib(N)
    print(answer)