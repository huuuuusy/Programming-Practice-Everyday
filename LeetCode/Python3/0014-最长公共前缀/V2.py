""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    利用zip和set函数进行求解
结果：
    执行用时 : 84 ms, 在所有 Python3 提交中击败了11.93%的用户
    内存消耗 : 13.1 MB, 在所有 Python3 提交中击败了87.27%的用户
"""

class Solution:
    def longestCommonPrefix(self, strs):
        result = ""
        # zip函数将strs中的字符串按照最短的字符串逐字符比较
        for string in zip(*strs):
            #print(string)
            # set函数删除string中相同的元素
            set_string = set(string)
            #print(set_string)
            # 如果删除后的set_string长度为1,说明该元素在所有str中均出现
            if len(set_string) == 1:
                result += string[0]
            else:
                break
        return result

if __name__ == "__main__":
    input_list = ["flower","flow","flight"]

    answer = Solution().longestCommonPrefix(input_list)
    print(answer)