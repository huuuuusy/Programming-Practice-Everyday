""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    类似斐波那契数列，动态规划
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了68.02%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.22%的用户
"""

class Solution:
    def climbStairs(self, n):
        # 类似斐波那契数列的解法
        # 如果只有1个台阶，则返回1
        if n == 1:
            return 1
        dp = [1,2] # 初始状态是两个台阶，一阶有1种爬法(1)，二阶有2种爬法(1+1或者2)
        # 对于高阶，分别是上一阶和上上阶的爬法总和
        for i in range(2,n):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n-1]



if __name__ == "__main__":
    n = 3
    answer = Solution().climbStairs(n)
    print(answer)