""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.39
工具： python == 3.7.3
"""

"""
思路:
    类似卷集中padding的方式，补全周围，然后循环计算
结果：
    执行用时 : 824 ms, 在所有 Python3 提交中击败了51.67%的用户
    内存消耗 : 14 MB, 在所有 Python3 提交中击败了8.77%的用户
"""

class Solution:
    def imageSmoother(self, M):
        # 将原始的矩阵外圈补0.5,不能补0或1,可补其他值
        m = len(M[0])
        N = [[0.5]+i+[0.5] for i in M] # 先在左右两侧补0.5
        N = [[0.5]*(m+2)] + N + [[0.5]*(m+2)] # 再在上下两侧补0.5
        
        # 卷积
        for i in range(1,len(N)-1):
            for j in range(1,len(N[0])-1):
                # 循环计算原始矩阵的每一个元素和周围元素的和，total存储每个元素的周围9个元素
                total = [N[i-1][j-1],N[i][j-1],N[i+1][j-1],N[i-1][j],N[i][j],N[i+1][j],N[i-1][j+1],N[i][j+1],N[i+1][j+1]]
                sums,k = 0,0
                for _ in total: # 去除total中的0.5
                    if _ != 0.5:
                        sums += _
                    else:
                        k += 1
                M[i-1][j-1] = int(sums/(9-k))
        return M

if __name__ == "__main__":
    M = [[1,1,1],[1,0,1],[1,1,1]]
    answer = Solution().imageSmoother(M)
    print(answer)