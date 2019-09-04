""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    注意补数的含义，采用二进制计算
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了55.23%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def findComplement(self, num):
        return 2**(len(bin(num))-2)- 1 - num

if __name__ == "__main__":
    num = 5
    answer = Solution().findComplement(num)
    print(answer)