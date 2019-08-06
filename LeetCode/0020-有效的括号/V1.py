""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    利用栈求解，但是需要考虑所有的特殊情况，某些测试用例不好通过
结果：
    执行用时 : 56 ms, 在所有 Python3 提交中击败了51.64%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了5.51%的用户
"""

class Solution:
    def isValid(self, s):
        if s == '':
            return True
        if len(s) % 2 != 0:
            return False
        result = []
        for i in range(len(s)):
            if s[i] == '(':
                result.append(s[i])
            elif s[i] == ')' and len(result) > 0 and result[-1] == '(':
                result.pop()
            elif s[i] == '[':
                result.append(s[i])
            elif s[i] == ']' and len(result) > 0 and len(result) > 0 and result[-1] == '[':
                result.pop()
            elif s[i] == '{':
                result.append(s[i])
            elif s[i] == '}' and len(result) > 0 and result[-1] == '{':
                result.pop()
        if result == []:
            return True
        else:
            return False

if __name__ == "__main__":
    s = "(()])}[}[}[]][}}[}{})][[(]({])])}}(])){)((){"
    answer = Solution().isValid(s)
    print(answer)