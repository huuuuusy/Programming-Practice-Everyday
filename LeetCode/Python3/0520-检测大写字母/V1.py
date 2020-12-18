""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    直接用python自带的字符判定函数确定
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了88%的用户
    内存消耗 : 13.6 MB, 在所有 Python3 提交中击败了5.26%的用户
"""


class Solution:
    def detectCapitalUse(self, word):
        return word.upper()==word or word.lower()==word or word.title()==word

if __name__ == "__main__":
    word = "FlaG"
    answer = Solution().detectCapitalUse(word)
    print(answer)