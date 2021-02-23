""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    判断当前数字的index和value是否满足要求，若满足则检查下一个，若不满足则将当前数字移到最后等待再排序
结果：
    执行用时 : 688 ms, 在所有 Python3 提交中击败了5.23%的用户
    内存消耗 : 16 MB, 在所有 Python3 提交中击败了5.38%的用户
"""

class Solution:
    def sortArrayByParityII(self, A):
        i = 0
        while i < len(A):
            if i%2 == A[i]%2:
                i += 1
            else:
                A.append(A[i])
                A.pop(i)
        return A


if __name__ == "__main__":
    A = [4,2,5,7]
    answer = Solution().sortArrayByParityII(A)
    print(answer)