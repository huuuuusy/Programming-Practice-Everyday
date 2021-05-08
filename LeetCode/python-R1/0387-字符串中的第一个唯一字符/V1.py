""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    利用字典判断
结果：
    执行用时 : 176 ms, 在所有 Python3 提交中击败了57.03%的用户
    内存消耗 : 13.2 MB, 在所有 Python3 提交中击败了90.85%的用户
"""

class Solution:
    def firstUniqChar(self, s):
        d = {}
        for num in s:
            d[num] = d.get(num,0) + 1
        for key, value in d.items():
            if value == 1:
                return s.index(key)
        return -1

if __name__ == "__main__":
    s = "loveleetcode"
    answer = Solution().firstUniqChar(s)
    print(answer)
