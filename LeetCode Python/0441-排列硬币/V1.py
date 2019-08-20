""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    二分查找
结果：
    执行用时 : 56 ms, 在所有 Python3 提交中击败了82.41%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.41%的用户
"""

class Solution:
    def arrangeCoins(self, n):
        left = 0
        right = n 
        while left < right:
            mid = (left + right + 1) >> 1 # 右中位数
            if (mid + mid*mid) // 2 > n:
                right = mid - 1 # 右边界收缩
            else:
                left = mid
        return left

            

if __name__ == "__main__":
    n = 5
    answer = Solution().arrangeCoins(n)
    print(answer)
