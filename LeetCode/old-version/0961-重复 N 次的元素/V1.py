""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37.1
工具： python == 3.7.3
"""

"""
思路:
    直接统计
结果：
    执行用时 : 308 ms, 在所有 Python3 提交中击败了76.94%的用户
    内存消耗 : 15.2 MB, 在所有 Python3 提交中击败了5.54%的用户
"""

class Solution:
    def repeatedNTimes(self, A):
        for num in A:
            if A.count(num) == len(A)/2:
                return num


if __name__ == "__main__":
    A = [1,2,3,3]
    answer = Solution().repeatedNTimes(A)
    print(answer)


