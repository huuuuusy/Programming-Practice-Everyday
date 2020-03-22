""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路：
    参考官方解答
    https://leetcode-cn.com/problems/valid-sudoku/solution/you-xiao-de-shu-du-by-leetcode/
    利用哈希映射进行判断
    每个数字遍历一遍即可
结果：
    执行用时 : 64 ms, 在所有 Python3 提交中击败了85.08%的用户
    内存消耗 : 13 MB, 在所有 Python3 提交中击败了96.557%的用户
"""

class Solution:
    def isValidSudoku(self, board):
        # 初始化数据
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    # 利用整除判断当前数字属于哪一个子数独
                    box_index = (i // 3 ) * 3 + j // 3
                    # 将当前值和出现的次数写进每行/列/子数独的字典中
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1
                    # 检查当前值是否已经在之前的某个字典里出现过
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
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
