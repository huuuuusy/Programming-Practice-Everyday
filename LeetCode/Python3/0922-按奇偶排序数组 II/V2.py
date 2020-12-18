""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    利用zip函数进行计算
结果：
    执行用时 : 300 ms, 在所有 Python3 提交中击败了46.51%的用户
    内存消耗 : 16 MB, 在所有 Python3 提交中击败了5.38%的用户
"""

class Solution:
    def sortArrayByParityII(self, A):
        res1 = [i for i in A if not i%2] # 偶数
        res2 = [i for i in A if i%2] # 奇数
        return [i for n in zip(res1, res2) for i in n]


if __name__ == "__main__":
    A = [4,2,5,7]
    answer = Solution().sortArrayByParityII(A)
    print(answer)