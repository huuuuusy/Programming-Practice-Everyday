""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路：
    转置矩阵+矩阵按行翻转
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了80.70%的用户
    内存消耗 : 13 MB, 在所有 Python3 提交中击败了90.03%的用户
"""

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])        
        # 转置矩阵
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
        
        # 翻转行
        for i in range(n):
            matrix[i].reverse()
        return matrix
        
if __name__ == "__main__":
    matrix =[
            [1,2,3],
            [4,5,6],
            [7,8,9]
            ]
    answer = Solution().rotate(matrix)
    print(answer)
