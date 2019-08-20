""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路：
    直接调用find函数
结果：
    执行用时 : 68 ms, 在所有 Python3 提交中击败了35.12%的用户
    内存消耗 : 13.2 MB, 在所有 Python3 提交中击败了８0.78%的用户
"""

class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)

if __name__ == "__main__":
    haystack = "hello"
    needle = "ll "
    answer = Solution().strStr(haystack, needle)
    print(answer)