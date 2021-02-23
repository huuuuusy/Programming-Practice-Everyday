""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    采用异或的思路，统计异或后"1"的位置
结果：
    执行用时 : 60 ms, 在所有 Python3 提交中击败了55.23%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')

if __name__ == "__main__":
    x = 1
    y = 4
    answer = Solution().hammingDistance(x, y)
    print(answer)