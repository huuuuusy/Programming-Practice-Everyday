""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37.1
工具： python == 3.7.3
"""

"""
思路:
    使用哈希表
结果：
    执行用时 : 68 ms, 在所有 Python3 提交中击败了69.79%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def calculateTime(self, keyboard, word):
        # 字典存储键值位置
        d = {}
        for index, value in enumerate(keyboard):
            d[value] = d.get(value, 0) + index
        # 计算移动的距离
        res = d[word[0]]
        for i in range(1, len(word)):
            res += abs(d[word[i]] - d[word[i - 1]])
        return res


if __name__ == "__main__":
    keyboard = "pqrstuvwxyzabcdefghijklmno"
    word = "leetcode"
    answer = Solution().calculateTime(keyboard, word)
    print(answer)