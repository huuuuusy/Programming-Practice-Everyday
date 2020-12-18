""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    巧妙的想法，用字典将前两个数的和存入，然后遍历后两个和去找相反数
结果：
    执行用时 : 384 ms, 在所有 Python3 提交中击败了72.01%的用户
    内存消耗 : 33.8 MB, 在所有 Python3 提交中击败了98.68%的用户
"""

class Solution:
    def fourSumCount(self, A, B, C, D):
        n = len(A)
        if n == 0:
            return 0
        if n == 1:
            if A[0]+B[0]+C[0]+D[0] != 0:
                return 0
            else:
                return 1
        # 构建字典，存2个数的和
        d = {}
        res = 0
        # 遍历前两个数组
        # 判断有多少种和的组合
        for i in A:
            for j in B:
                d[i+j] = d.get(i+j,0) + 1
        # 遍历后两个数组
        # 如果和的相反数在字典中，则将结果加入到res中
        for i in C:
            for j in D:
                if -(i+j) in d:
                    res += d[-(i+j)]
        return  res


if __name__ == "__main__":
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    answer = Solution().fourSumCount(A, B, C, D)
    print(answer)
