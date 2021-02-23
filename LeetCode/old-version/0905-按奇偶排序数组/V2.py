""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    使用双指针，不使用额外空间，直接原址交换数值进行修改
结果：
    执行用时 : 124 ms, 在所有 Python3 提交中击败了24.23%的用户
    内存消耗 : 14.4 MB, 在所有 Python3 提交中击败了5.38%的用户
"""

class Solution:
    def sortArrayByParity(self, A):
        i, j = 0, len(A)-1
        while i < j:
            while A[i]%2 == 0 and  i < j:
                i += 1 
            while A[j]%2 == 1 and i < j:
                j -= 1
            A[i], A[j] = A[j], A[i]
        return A


if __name__ == "__main__":
    A = [3,1,2,4]
    answer = Solution().sortArrayByParity(A)
    print(answer)