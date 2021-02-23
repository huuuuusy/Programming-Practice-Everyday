""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    用字典保存每个元素出现的次数，然后倒序判断是否有最大唯一数
结果：
    执行用时 : 68 ms, 在所有 Python3 提交中击败了77.23%的用户
    内存消耗 : 14 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def largestUniqueNumber(self, A):
        d = {}
        for index, value in enumerate(A):
            d[value] = d.get(value,0) + 1
        for key in sorted(d.keys())[::-1]:
            if d[key] > 1:
                continue
            else:
                return key
        return -1

if __name__ == "__main__":
    A = [9,9,8,8]
    answer = Solution().largestUniqueNumber(A)
    print(answer)