""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    简单题
结果：
    执行用时 : 44 ms, 在所有 Python3 提交中击败了92.08%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.05%的用户
"""

class Solution:
    def numJewelsInStones(self, J, S):
        if len(J) == 0 or len(S) == 0:
            return 0
        num = 0 
        for s in list(S):
            if s in list(J):
                num += 1 
        return num 

if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"
    answer = Solution().numJewelsInStones( J, S)
    print(answer)