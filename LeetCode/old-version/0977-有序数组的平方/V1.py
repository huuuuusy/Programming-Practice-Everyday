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
    执行用时 : 304 ms, 在所有 Python3 提交中击败了31.77%的用户
    内存消耗 : 15.8 MB, 在所有 Python3 提交中击败了5.25%的用户
"""

class Solution:
    def sortedSquares(self, A):
        square = [x*x for x in A]
        return sorted(square)

if __name__ == "__main__":
    A = [-4,-1,0,3,10]
    answer = Solution().sortedSquares(A)
    print(answer)