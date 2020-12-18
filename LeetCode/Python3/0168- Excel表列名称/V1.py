""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    转化为26进制计算，注意65~90为大写字母
结果：
    执行用时 : 40 ms, 在所有 Python3 提交中击败了93.15%的用户
    内存消耗 : 13.7MB, 在所有 Python3 提交中击败了5.19%的用户
"""

class Solution:
    def convertToTitle(self, n):
        res = ''
        while n:
            n -= 1
            n, y = divmod(n, 26) # n和y分别存储n除以26后的商和余数
            res = chr(y+65) + res
        return res       

if __name__ == "__main__":
    n = 1
    answer = Solution().convertToTitle(n)
    print(answer)