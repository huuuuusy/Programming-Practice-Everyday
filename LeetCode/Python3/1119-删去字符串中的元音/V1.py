""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    无难度
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了35.23%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def removeVowels(self, S):
        vowels = ['a', 'e', 'i', 'o', 'u']
        target = "".join([x for x in list(S) if x not in vowels])
        return target

if __name__ == "__main__":
    S = "leetcodeisacommunityforcoders"
    answer = Solution().removeVowels(S)
    print(answer)