""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    理清思路，巧用循环
结果：
    执行用时 : 140 ms, 在所有 Python3 提交中击败了92.08%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.05%的用户
"""

class Solution:
    def shortestToChar(self, S, C):
        c_pos = [i for i in range(len(S)) if C == S[i]]
        res = []
        for i in range(len(S)):
            res.append(min(abs(i - j) for j in c_pos))
        return res

if __name__ == "__main__":
    S = "loveleetcode"
    C = 'e'
    answer = Solution().shortestToChar(S, C)
    print(answer)