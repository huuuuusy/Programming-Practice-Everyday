""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    1. 和前一个颜色相同，此时说明前一个的栅栏的颜色应与更前面一个栅栏的颜色不同，更前一个栅栏的涂色方法有 F(n - 2) 种，前一个栅栏的涂色方式有 (k - 1) 种，所以此时情况应为 F(n - 2) * (k - 1)
    2. 和前一个颜色不同，前一个栅栏的涂色方法有 F(n - 1) 种，当前栅栏的涂色方式有 (k - 1) 种，此时情况应为 F(n - 1) * (k - 1)
    所以递推公式应为 F(n) = F(n - 2) * (k - 1) + F(n - 1) * (k - 1)
结果：
    执行用时 : 36 ms, 在所有 Python3 提交中击败了98.89%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def numWays(self, n, k):
        if n == 0 or k == 0: return 0
        if n == 1: return k
        res = [k, k*k] # 如果只有一个栏杆，有k种；如果有两个栏杆，有k*k种
        for i in range(2,n):
            res.append(res[-1]*(k-1) + res[-2]*(k-1))
        return res[-1]


if __name__ == "__main__":
    n = 3
    k = 2
    answer = Solution().numWays(n, k)
    print(answer)