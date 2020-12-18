""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    直接调python自带的小写转换函数
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了85.41%的用户
    内存消耗 : 15.2 MB, 在所有 Python3 提交中击败了86.15%的用户
"""

class Solution:
    def toLowerCase(self, str):
        return str.lower()

if __name__ == "__main__":
    nums =  "Hello"
    answer = Solution().toLowerCase(nums)
    print(answer)