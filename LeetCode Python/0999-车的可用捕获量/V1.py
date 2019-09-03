""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    理解题意则不复杂
结果：
    执行用时 : 40 ms, 在所有 Python3 提交中击败了97.15%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了5%的用户
"""

class Solution:
    def numRookCaptures(self, board):
        row = {}
        col = {}
        # 得到所有行列
        for i in range(len(board)):
            row[i] = board[i]
        for i in range(len(board)):
            for j in range(len(board[0])):
                col[j] = col.get(j,[]) + [board[i][j]]
                if board[i][j] == 'R':
                    rock_row, rock_col = i, j
        # 取出目标行列            
        check_row = row[rock_row]
        check_col = col[rock_col]
        res = 0
        # 检查目标行
        left = rock_col-1
        right = rock_col+1
        while left >= 0:
            if check_row[left] == 'p':
                res += 1
                break
            elif check_row[left] == 'B':
                break
            left -= 1
        while right <= len(board)-1:
            if check_row[right] == 'p':
                res += 1
                break
            elif check_row[right] == 'B':
                break
            right += 1
        # 检查目标列
        left = rock_row-1
        right = rock_row+1
        while left >= 0:
            if check_col[left] == 'p':
                res += 1
                break
            elif check_col[left] == 'B':
                break
            left -= 1
        while right <= len(board)-1:
            if check_col[right] == 'p':
                res += 1
                break
            elif check_col[right] == 'B':
                break
            right += 1
        return res

if __name__ == "__main__":
    board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    answer = Solution().numRookCaptures(board)
    print(answer)