""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路：
    直接对每种情况的9个数字进行处理：
        删除"."
        判断纯数字列表中是否有重复数字，利用set()函数
结果：
    执行用时 : 72 ms, 在所有 Python3 提交中击败了54.37%的用户
    内存消耗 : 12.9 MB, 在所有 Python3 提交中击败了85.17%的用户
"""

class Solution:
    def isValidSudoku(self, board):
        # 判断每行是否有重复数字
        for i in range(0, 9):
            row = [x for x in board[i] if x != '.']
            if len(set(row)) != len(row):
                return False

        # 判断每列是否有重复数字
        for j in range(0,9):
            col = []
            for i in range(0,9):
                col.append(board[i][j])
            new_col = [x for x in col if x != '.']
            if len(set(new_col)) != len(new_col):
                return False

        # 判断每个3×3格子是否有重复数字
        for i in range(0,3):
            for j in range(0,3):
                mini = []
                mini.append(board[3*i][3*j])
                mini.append(board[3*i][3*j+1])
                mini.append(board[3*i][3*j+2])
                mini.append(board[3*i+1][3*j])
                mini.append(board[3*i+1][3*j+1])
                mini.append(board[3*i+1][3*j+2])
                mini.append(board[3*i+2][3*j])
                mini.append(board[3*i+2][3*j+1])
                mini.append(board[3*i+2][3*j+2])
                new_mini = [x for x in mini if x != '.']
                if len(set(new_mini)) != len(new_mini):
                    return False
        return True

if __name__ == "__main__":
    board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    answer = Solution().isValidSudoku(board)
    print(answer)
