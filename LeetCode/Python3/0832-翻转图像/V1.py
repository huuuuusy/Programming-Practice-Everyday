""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    最内层循环反转，第二层循环翻转，最外层循环遍历每一行
结果：
    执行用时 : 80 ms, 在所有 Python3 提交中击败了35.66%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了5.48%的用户
"""

class Solution:
    def flipAndInvertImage(self, A):
        return [[j ^ 1 for j in row[::-1]] for row in A]

if __name__ == "__main__":
    A = [[1,1,0],[1,0,1],[0,0,0]]
    answer = Solution().flipAndInvertImage(A)
    print(answer)