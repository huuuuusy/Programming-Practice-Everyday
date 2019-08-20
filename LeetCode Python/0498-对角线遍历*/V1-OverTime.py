""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    先列出来元素下标的规律，然后根据下标规律分情况讨论
注意：
    需要讨论各种情况
    因为原始思路是把矩阵先作方阵处理，所以对于一行或者一列的矩阵，展开成方阵再剔除元素会很容易超时
结果：
    第22个测试用例超时
"""

class Solution:
    def findDiagonalOrder(self, matrix):
        # 排除空矩阵
        if matrix == []:
            return []
        # m,n分别是矩阵的长和宽
        m = len(matrix)
        n = len(matrix[0])
        max_num = max(m, n)
        # remain_list存储矩阵元素下标的取值范围
        remain_list = list(range(max_num))
        # index_list存储按对角线规则遍历矩阵时读取下标的顺序
        # 此时先把所有矩阵当做方阵处理
        index_list= []
        for i in range(m + n -1):
            for j in remain_list:
                if i-j in remain_list:
                    if i % 2 == 1:
                        index_list.append([j, i-j])
                    else:
                        index_list.append([i-j, j])
        result = []
        # 在最后写入结果时排除下标范围不属于矩阵的元素
        for k in index_list:
            k0 = k[0]
            k1 = k[1]
            if k[0] < m and k[1] < n:
                result.append(matrix[k0][k1])
        return result

if __name__ == "__main__":
    nums =  [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
    answer = Solution().findDiagonalOrder(nums)
    print(answer)