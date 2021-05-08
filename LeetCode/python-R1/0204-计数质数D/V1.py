""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.39
工具： python == 3.7.3
"""

"""
思路:
    厄拉多塞筛法
    https://leetcode-cn.com/problems/count-primes/solution/qiu-zhi-shu-chao-guo-90-by-powcai/
结果：
    执行用时 : 2660 ms, 在所有 Python3 提交中击败了5.50%的用户
    内存消耗 : 25.3 MB, 在所有 Python3 提交中击败了64.17%的用户
"""
class Solution:
    def countPrimes(self, n):
        isPrimes = [1] * n # 置1表示是质数
        res = 0
        for i in range(2, n):
            if isPrimes[i] == 1: res += 1
            j = i
            while i * j < n: # 置0表示非质数
                isPrimes[i * j] = 0
                j += 1
        return res




if __name__ == "__main__":
    n = 10
    answer = Solution().countPrimes(n)
    print(answer)