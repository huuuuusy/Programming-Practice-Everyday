""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    先rstrip去右边空格，再split空格，取最后一个单词的长度
结果：
    执行用时 : 56 ms, 在所有 Python3 提交中击败了35.48%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.54%的用户
"""

class Solution:
    def lengthOfLastWord(self, s):
        return len(s.rstrip().split(" ")[-1])

if __name__ == "__main__":
    s = "a "
    answer = Solution().lengthOfLastWord(s)
    print(answer)
