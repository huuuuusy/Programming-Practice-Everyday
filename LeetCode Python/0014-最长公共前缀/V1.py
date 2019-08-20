""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    从列表中取出长度最短的第一个字符串
    依次和其余字符串进行比对
结果：
    执行用时 : 84 ms, 在所有 Python3 提交中击败了11.93%的用户
    内存消耗 : 13.1 MB, 在所有 Python3 提交中击败了87.27%的用户
"""

class Solution:
    def longestCommonPrefix(self, strs):
        # 先排除两种特殊情况
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        # 从输入中拿出第一个长度最短的字符串
        length_list = [len(string) for string in strs]
        min_index = length_list.index(min((length_list)))
        min_str = strs[min_index]
        strs.pop(min_index)
        # 依次和其余字符串进行比对
        for i in range(len(min_str)):
            prefix = min_str[:i+1]
            for string in strs:
                if string[:i+1] != prefix:
                    return prefix[:i]
        return min_str

if __name__ == "__main__":
    input_list = ["dog",'dog']
    answer = Solution().longestCommonPrefix(input_list)
    print(answer)