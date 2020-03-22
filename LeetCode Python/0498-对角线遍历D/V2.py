""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    按照实际遍历的情况判断是否到达边界
    如果到达边界则转换方向
注意：
    需要讨论各种情况
    分析清楚遍历的规律后则程序很简单
结果：
    执行用时 : 148 ms, 在所有 Python3 提交中击败了92.03%的用户
    内存消耗 : 15.2 MB, 在所有 Python3 提交中击败了92.59%的用户
"""
class Solution:
    def findDiagonalOrder(self, matrix):
        # 排除空矩阵
        if matrix == []:
            return []
        # row表示行，col表示列
        row = len(matrix)
        col = len(matrix[0])
        # 如果是一行的矩阵，直接返回第一行的值
        if row == 1:
            return matrix[0]
        # result保存最终结果
        result = []
        # number存储需要循环的次数
        number = row * col
        # up是是否向右上查看的标识
        up = True
        i = j = 0
        while number:
            number -= 1
            result.append(matrix[i][j])
            # 如果向右上遍历
            if up == True:
                # 如果到达最右边
                # 需要改变遍历方向，向左下遍历
                if j == col - 1:
                    up = False
                    i += 1
                # 如果到达最上边
                # 需要改变遍历方向，向左下遍历
                elif i == 0:
                    up = False
                    j += 1
                # 如果没有到达边界
                # 保持遍历方向，继续向右上遍历
                else:
                    i -= 1
                    j += 1

            # 如果向左下遍历
            else:
                # 如果到达最下边
                # 需要改变遍历方向，向右上遍历
                if i == row - 1:
                    up = True
                    j += 1
                # 如果到达最左边
                # 需要改变遍历方向，向右上遍历
                elif j == 0:
                    up = True
                    i += 1
                # 如果没有到达边界
                # 保持遍历方向，继续向右上遍历
                else:
                    i += 1
                    j -= 1
        
        return result


if __name__ == "__main__":
    nums =  [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
    answer = Solution().findDiagonalOrder(nums)
    print(answer)