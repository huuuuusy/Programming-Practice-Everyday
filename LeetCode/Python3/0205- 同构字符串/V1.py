""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    先用set从长度上判断
    然后再用字典进行判别
结果：
    执行用时 : 56 ms, 在所有 Python3 提交中击败了91.68%的用户
    内存消耗 : 13.2 MB, 在所有 Python3 提交中击败了87.42%的用户
"""

class Solution:
    def isIsomorphic(self, s, t):
        d = {}
        if len(set(s)) != len(set(t)) or len(s) != len(t):
            return False
        for i in range(len(s)):
            if d.__contains__(s[i]):
                if d[s[i]] != t[i]:
                    return False
                else:
                    continue
            d[s[i]] = t[i]
        return True
        

if __name__ == "__main__":
    s = "ab"
    t = "aa"
    answer = Solution().isIsomorphic(s, t)
    print(answer)