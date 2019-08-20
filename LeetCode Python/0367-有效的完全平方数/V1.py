""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    二分法
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了77.13%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了5.30%的用户
"""

class Solution:
    def isPerfectSquare(self, num):
        # 先排除四种特殊情况，这4种数的整除2之后的值的平方不大于其本身
        if num == 1 or num == 4:
            return True
        if num == 2 or num == 3:
            return False 
        # 二分法
        left = 0 
        right = num 
        while left < right:
            mid = (left + right + 1) >> 1 # 右中位数
            if mid * mid > num:
                right = mid - 1　# 右边界收缩
            else:
                left = mid 
        if left * left == num:
            return True
        else:
            return False

if __name__ == "__main__":
    num = 14
    answer = Solution().isPerfectSquare(num)
    print(answer)

