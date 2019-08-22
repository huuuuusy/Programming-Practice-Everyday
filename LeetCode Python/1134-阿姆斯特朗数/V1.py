""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37.1
工具： python == 3.7.3
"""

"""
思路:
    python直接解法，利用列表取出每一位数字判断
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了66.23%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def isArmstrong(self, N):
        nums = list(str(N))
        k = len(nums)
        res = 0
        for num in nums:
            res += int(num)**k
        return True if res == N else False
         
if __name__ == "__main__":
    N = 123
    answer = Solution().isArmstrong(N)
    print(answer)