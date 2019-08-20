""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    用字典存储移位数字
注意：
    flag首先添加一位str(len(value)),为了区分0,1,1和0,11
结果：
    执行用时 : 56 ms, 在所有 Python3 提交中击败了90.91%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def groupStrings(self, strings):
        d = {}
        # 计算每一位和第一个的差值
        for index, value in enumerate(strings):
            # flag首先添加一位str(len(value)),为了区分0,1,1和0,11
            flag = str(len(value))
            for i in range(len(value)):
                # 用ord()计算移位字母
                flag += str((ord(value[i]) - ord(value[0]))%26)
            d[flag] = d.get(flag,[]) + [value]
        result = []
        for key, value in d.items():
            result.append(value)
        return result

if __name__ == "__main__":
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    answer = Solution().groupStrings(strings)
    print(answer)


