""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    检索时，如果每行第j个元素已经大于target，则下一行检索到j即可
结果：
    执行用时 : 56 ms, 在所有 Python3 提交中击败了78.04%的用户
    内存消耗 : 18.3 MB, 在所有 Python3 提交中击败了5.18%的用户
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] > target:
                    col = j
                    break
                elif matrix[i][j] == target:
                    return True
        return False

if __name__ == "__main__":
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
        ]
    target = 16
    answer = Solution().searchMatrix(matrix, target)
    print(answer)