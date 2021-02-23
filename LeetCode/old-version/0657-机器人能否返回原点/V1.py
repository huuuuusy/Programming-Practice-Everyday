""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    简单的方法，无难度
结果：
    执行用时 : 92 ms, 在所有 Python3 提交中击败了36.03%的用户
    内存消耗 : 14.1 MB, 在所有 Python3 提交中击败了5.32%的用户
"""

class Solution:
    def judgeCircle(self, moves):
        if len(list(moves))%2 == 1:
            return False
        width = 0
        height = 0
        for move in list(moves):
            if move == 'R':
                width += 1
            elif move =='L':
                width -= 1
            elif move == 'U':
                height += 1
            elif move == 'D':
                height -= 1
        if width == 0 and height == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    moves = 'UDU'
    answer = Solution().judgeCircle(moves)
    print(answer)