""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    理解题意则不复杂
结果：
    执行用时 : 220 ms, 在所有 Python3 提交中击败了15.23%的用户
    内存消耗 : 14.9 MB, 在所有 Python3 提交中击败了6%的用户
"""

class Solution:
    def smallestRangeI(self, A, K):
        left = sorted(A)[0] + K
        right = sorted(A)[-1] - K
        return right - left if left <= right else 0

if __name__ == "__main__":
    A = [0,10]
    K = 6
    answer = Solution().smallestRangeI(A, K)
    print(answer)