""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    简单题
结果：
    执行用时 : 104 ms, 在所有 Python3 提交中击败了56.37%的用户
    内存消耗 : 14.6 MB, 在所有 Python3 提交中击败了5.21%的用户
"""

class Solution:
    def transpose(self, A):
        row = len(A)
        col = len(A[0])
        res = []
        for i in range(col):
            res_mini = []
            for j in range(row):
                res_mini.append(A[j][i])
            res.append(res_mini)
        return res


if __name__ == "__main__":
    A = [[1,2,3],[4,5,6]]
    answer = Solution().transpose(A)
    print(answer)