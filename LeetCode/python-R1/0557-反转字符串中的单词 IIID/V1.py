""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    两次反转
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了86.14%的用户
    内存消耗 : 13.3 MB, 在所有 Python3 提交中击败了93.84%的用户
"""

class Solution:
    def reverseWords(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        s = " ".join(s.split(' ')[::-1])[::-1]
        return s


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    answer = Solution().reverseWords(s)
    print(answer)