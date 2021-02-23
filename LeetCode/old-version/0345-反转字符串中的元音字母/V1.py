""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    两轮单循环
结果：
    执行用时 : 96 ms, 在所有 Python3 提交中击败了42.08%的用户
    内存消耗 : 15.2 MB, 在所有 Python3 提交中击败了15.61%的用户
"""

class Solution:
    def reverseVowels(self, s):
        vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels = []
        for string in list(s):
            if string in vowels_list:
                vowels.append(string)
        res = ""
        for string in list(s):
            if string in vowels_list:
                string = vowels.pop()
            res += string
        return res
        
if __name__ == "__main__":
    s = "aA"
    answer = Solution().reverseVowels(s)
    print(answer)