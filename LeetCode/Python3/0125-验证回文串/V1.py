""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    小写转换+翻转判断
结果：
    执行用时 : 64 ms, 在所有 Python3 提交中击败了91.66%的用户
    内存消耗 : 15.2 MB, 在所有 Python3 提交中击败了11.60%的用户
"""

class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        a = list(s)
        new_s = []
        for num in a:
            if 'a' <= num <= 'z' or '0' <= num <= '9':
                new_s.append(num)
        if new_s == new_s[::-1]:
            return True
        return False

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    answer = Solution().isPalindrome(s)
    print(answer)