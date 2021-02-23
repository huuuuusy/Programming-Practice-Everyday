""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    使用迭代器
结果：
    执行用时 : 108 ms, 在所有 Python3 提交中击败了68.03%的用户
    内存消耗 : 18.2 MB, 在所有 Python3 提交中击败了5.26%的用户
"""

class Solution:
    def isSubsequence(self, s, t):
        t = iter(t)
        return all(i in t for i in s)

if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    answer = Solution().isSubsequence(s, t)
    print(answer)
