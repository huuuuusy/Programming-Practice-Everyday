""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    代码简单，但是关键是理解题意：
    注意题目中的独有两个字：
        s1 = 'ab',s2 = 'a',因为ab是s1独有，所以最长子序列为ab；
        s1 = 'ab', s2 = 'ab', 因为ab是两个串都有，ab排除，a也是两个串都有，排除，b也是两个串都有，排除。所以最长特殊序列不存在，返回-1；
    通过以上分析，我们可以得出结论，如果：两个串相等（不仅长度相等，内容也相等），那么他们的最长特殊序列不存在。返回-1；
    如果两个串长度不一样，那么长的串 永远也不可能是 短串的子序列，即len(s1) > len(s2),则最长特殊序列为s1,返回长度大的数。
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了75%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了6.40%的用户
"""

class Solution:
    def findLUSlength(self, a, b):
        if a == b:
            return -1
        else:
            return len([a if len(a) > len(b) else b][0])
        

if __name__ == "__main__":
    a = "aba"
    b = "cdc"
    answer = Solution().findLUSlength(a, b)
    print(answer)


