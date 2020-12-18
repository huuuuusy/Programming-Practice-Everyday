""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    分割＋反转
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了76.13%的用户
    内存消耗 : 13.3 MB, 在所有 Python3 提交中击败了70.90%的用户
"""

class Solution:
    def reverseWords(self, s):
        s = s.split()
        s.reverse()
        result = " ".join(s)
        return result


if __name__ == "__main__":
    s = "  hello world!  "
    answer = Solution().reverseWords(s)
    print(answer)