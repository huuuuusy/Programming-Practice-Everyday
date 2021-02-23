""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    无难度,直接解法的时空性能都一般
结果：
    执行用时 : 124 ms, 在所有 Python3 提交中击败了24.23%的用户
    内存消耗 : 14.5 MB, 在所有 Python3 提交中击败了5.38%的用户
"""

class Solution:
    def sortArrayByParity(self, A):
        res = []
        for i in range(len(A)):
            num = A.pop()
            if num % 2 == 1:
                res.append(num)
            else:
                res.insert(0, num)
        return res

if __name__ == "__main__":
    A = [3,1,2,4]
    answer = Solution().sortArrayByParity(A)
    print(answer)