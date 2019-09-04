""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    注意用set()的巧妙处理
结果：
    执行用时 : 56 ms, 在所有 Python3 提交中击败了97.15%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了5%的用户
"""

class Solution:
    def commonChars(self, A):
        res = []
        if len(A) < 2:
            return res
        key = set(A[0])
        for k in key:
            minnum = min(a.count(k) for a in A)
            res += minnum*k
        return res

if __name__ == "__main__":
    A = ["bella","label","roller"]
    answer = Solution().commonChars( A)
    print(answer)