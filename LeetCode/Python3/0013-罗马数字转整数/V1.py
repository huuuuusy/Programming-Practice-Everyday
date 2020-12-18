""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    简单的思路，直接列出所有情况判断
结果：
    执行用时 : 76 ms, 在所有 Python3 提交中击败了88%的用户
    内存消耗 : 14.1 MB, 在所有 Python3 提交中击败了5.25%的用户
"""

class Solution:
    def romanToInt(self, s):
        if s == "":
            return 0
        sum = 0
        string = list(s)
        i = 0
        while i < len(string):
            if string[i] == 'I':
                if i+1 < len(string):
                    if string[i+1] == 'V':
                        sum += 4
                        i += 2
                        continue 
                    elif string[i+1] == 'X':
                        sum += 9
                        i += 2 
                        continue
                sum += 1 
            elif string[i] == 'V':
                sum += 5 
            elif string[i] == 'X':
                if i+1 < len(string):
                    if string[i+1] == 'L':
                        sum += 40
                        i += 2 
                        continue 
                    elif string[i+1] == 'C':
                        sum += 90
                        i += 2 
                        continue
                sum += 10
            elif string[i] == 'L':
                sum += 50
            elif string[i] == 'C':
                if i+1 < len(string):
                    if string[i+1] == 'D':
                        sum += 400
                        i += 2 
                        continue 
                    elif string[i+1] == 'M':
                        sum += 900
                        i += 2 
                        continue
                sum += 100
            elif string[i] == 'D':
                sum += 500
            elif string[i] == 'M':
                sum += 1000 
            i += 1
        return sum
        
if __name__ == "__main__":
    s = 'LVIII'
    answer = Solution().romanToInt(s)
    print(answer)