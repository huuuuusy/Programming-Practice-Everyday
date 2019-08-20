""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
"""

"""
思路:
    用四个标识符进行方向判别
    用四个数字分别统计四个方向遍历的次数
    分析清楚每一种情况
注意:
    注意第一次向右向下向左均以矩阵边缘作为边界，但是第一次向上的边界是第二行而非第一行
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了69.90%的用户
    内存消耗 : 12.9 MB, 在所有 Python3 提交中击败了99.11%的用户
"""

class Solution:
    def spiralOrder(self, matrix):
        # 排除空矩阵
        if matrix == []:
            return []
        # m, n是矩阵的行列数
        m = len(matrix)
        n = len(matrix[0])
        # 四个方向的判别
        left = False
        right = True
        up = False
        down = False
        # 每个方向已经经过的次数
        # 因为第二次经过该方向时终止的边界会改变
        left_num =0
        right_num = 0
        up_num = 0
        down_num = 0
        result = []
        i = 0
        j = 0
        for k in range(m*n):
            # 向右
            if right == True:
                result.append(matrix[i][j]) 
                j += 1
                # 如果到达右边界
                # 方向变为向下
                # 向右的次数加一
                if j == n - right_num:
                    right = False
                    down = True
                    right_num += 1
                    j -= 1
                    i += 1
                    continue
            # 向下
            if down == True:
                result.append(matrix[i][j]) 
                i += 1
                # 如果到达下边界
                # 方向变为向左
                # 向下的次数加一
                if i == m - down_num:
                    down = False
                    left = True
                    down_num += 1
                    i -= 1
                    j -= 1
                    continue
            # 向左
            if left == True:
                result.append(matrix[i][j]) 
                j -= 1
                # 如果到达左边界
                # 方向变为向上
                # 向左的次数加一
                if j == -1 + left_num:
                    left = False
                    up = True
                    left_num += 1
                    j += 1
                    i -= 1
                    continue
            # 向上
            if up == True:
                result.append(matrix[i][j]) 
                i -= 1
                # 如果到达上边界
                # 方向变为向右
                # 向上的次数加一
                # 注意这里是0+up_num而非-1+up_num，因为第一次向上就无法到达顶端（第一行已经在向右时遍历过）
                if i == 0 + up_num:
                    up = False
                    right = True
                    up_num += 1
                    i += 1
                    j += 1
                    continue
        return result

if __name__ == "__main__":
    nums =  [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
    answer = Solution().spiralOrder(nums)
    print(answer)