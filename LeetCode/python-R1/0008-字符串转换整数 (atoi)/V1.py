""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路：
    分清每种情况，非常容易漏掉特殊的输入
结果：
    执行用时 : 40 ms, 在所有 Python3 提交中击败了99.78%的用户
    内存消耗 : 13.1 MB, 在所有 Python3 提交中击败了91.91%的用户
"""

class Solution:
    def myAtoi(self, str):
        list_str = list(str.strip())
        flag = True
        result = []
        if list_str == []:
            return 0
        if (list_str[0] < '0' or list_str[0] > '9') and list_str[0] != '-' and list_str[0] != '+':
            return 0
        if list_str[0] == '-':
            new_list = list_str[1:]
            flag = False
            if new_list == []:
                return 0
        elif list_str[0] == '+':
            new_list = list_str[1:]
            if new_list == []:
                return 0
        else:
            new_list = list_str
        for num in new_list:
            if '0' <= num <= '9':
                result.append(num)
            else:
                break
        if result == []:
            return 0
        result_num = int(''.join(result))
        if flag == False:
            result_num = -result_num
        if result_num < -2**31:
            return -2**31
        elif result_num > 2**31 -1:
            return 2**31 -1
        return result_num   

if __name__ == "__main__":
    str = "   +42"
    answer = Solution().myAtoi(str)
    print(answer)
