""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    转化为26进制计算，注意65~90为大写字母，97~122为小写字母
结果：
    执行用时 : 40 ms, 在所有 Python3 提交中击败了98.15%的用户
    内存消耗 : 14 MB, 在所有 Python3 提交中击败了6%的用户
"""

class Solution:
    def titleToNumber(self, s):
        s = s[::-1]
        sum = 0
        for index, value in enumerate(s):
            sum += (ord(value) - 64)*26**index # 转化为26进制
        return sum

        

if __name__ == "__main__":
    s = "ZY"
    answer = Solution().titleToNumber(s)
    print(answer)