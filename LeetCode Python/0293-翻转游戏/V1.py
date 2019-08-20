""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    无难度
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了71.4%的用户
    内存消耗 : 14 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def generatePossibleNextMoves(self, s):
        res = []
        for i in range(len(s) - 1):
            if s[i:i+2] == "++":
                res.append(s[:i] + "--" + s[i+2:])
        return res
        
if __name__ == "__main__":
    s = "++++"
    answer = Solution().generatePossibleNextMoves(s)
    print(answer)