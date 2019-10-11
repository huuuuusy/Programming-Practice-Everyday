""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.39
工具： python == 3.7.3
"""

"""
思路:
    直接暴力求解会超时
    如果需要产生零，阶乘中的数需要包含 2 和 5 这两个因子，只要数一数组成阶乘的数中共有多少对 2 和 5 的组合即可
    又因为 5 的个数一定比 2 少，问题简化为计算 5 的个数就可以了
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了68.15%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.19%的用户
"""

class Solution:
    def trailingZeroes(self, n):
        res = 0
        while n >= 5:
            res += int(n/5)
            n /= 5
        return res     

if __name__ == "__main__":
    n = 5
    answer = Solution().trailingZeroes(n)
    print(answer)