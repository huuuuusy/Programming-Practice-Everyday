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
    执行用时 : 52 ms, 在所有 Python3 提交中击败了67.42%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def fixedPoint(self, A):
        if A == []:
            return -1
        for i in range(len(A)):
            if A[i] == i:
                return i
        else:
            return -1

        


if __name__ == "__main__":
    A = [-10,-5,0,3,7]
    answer = Solution().fixedPoint(A)
    print(answer)