""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路：
    以每个元素为中心，分别向外扩散寻找奇数回文子串和偶数回文子串
结果：
    执行用时 : 868 ms, 在所有 Python3 提交中击败了82.03%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了19.28%的用户
"""

class Solution:
    def longestPalindrome(self, s):
        def help(s, left, right):
            """
            1. 针对s, 从left向左扩散, right向右扩散, 得到当前最大的回文子串
            2. 返回其子串的长度
            """
            N = len(s)
            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
    
        if not s:
            return ""
        start, end = 0, 0
        for i in range(len(s)):
            # 分别以s中的每个字母为中心进行扩散判断
            # 回文子串存在奇数和偶数两种情况
            # 分别以help(s, i, i)表示奇数子串（以s[i]为扩散中心),以help(s, i, i + 1)表示偶数子串（以s[i]s[i+1]表示扩散中心)
            len1, len2 = help(s, i, i), help(s, i, i + 1)
            len0 = max(len1, len2)
            if len0 > end - start:
                # 定位到当前子串的start, end索引
                start = i - (len0 - 1) // 2
                end = i + len0 // 2
        return s[start:end + 1]


if __name__ == "__main__":
    s = "babad"
    answer = Solution().longestPalindrome(s)
    print(answer)
