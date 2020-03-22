""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.39
工具： python == 3.7.3
"""

"""
思路:
    使用哈希表
结果：
    执行用时 : 40 ms, 在所有 Python3 提交中击败了92.03%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了5.26%的用户
"""

class Solution:
    def validWordAbbreviation(self, word, abbr):
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            #print(i, j)
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit():
                if abbr[j] == "0": return False
                tmp = ""
                while j < len(abbr) and abbr[j].isdigit():
                    tmp += abbr[j]
                    j += 1
                #print(tmp)
                i += int(tmp)
            else:
                return False

        return i == len(word) and j == len(abbr)

if __name__ == "__main__":
    word = "internationalization"
    abbr = "i12iz4n"
    answer = Solution().validWordAbbreviation(word, abbr)
    print(answer)
