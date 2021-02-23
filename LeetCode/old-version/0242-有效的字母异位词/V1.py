""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    用set()函数排除重复元素
    用count()函数统计出现的次数
注意：
    用set()可以极大提升效率
结果：
    执行用时 : 44 ms, 在所有 Python3 提交中击败了99.73%的用户
    内存消耗 : 13.2 MB, 在所有 Python3 提交中击败了92.69%的用户
"""

class Solution:
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        if s==t and s=="":
            return True
        for num in set(s):
            if s.count(num) != t.count(num):
                return False
        return True


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    answer = Solution().isAnagram(s, t)
    print(answer)