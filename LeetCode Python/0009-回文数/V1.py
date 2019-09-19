""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路：
    简单题
结果：
    执行用时 : 96 ms, 在所有 Python3 提交中击败了62.78%的用户
    内存消耗 : 14.1 MB, 在所有 Python3 提交中击败了5.01%的用户
"""

class Solution:
    def isPalindrome(self, x):
        return True if list(str(x)) == list(str(x))[::-1] else False

if __name__ == "__main__":
    x = 121
    answer = Solution().isPalindrome(x)
    print(answer)
