""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    简单题,但是还可以进一步优化时间
结果：
    执行用时 : 104 ms, 在所有 Python3 提交中击败了14.29%的用户
    内存消耗 : 17.3 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def shortestDistance(self, words, word1, word2):
        # 字典存储索引
        d = {}
        for index, value in enumerate(words):
            d[value] = d.get(value,[]) + [index]
        index1s = d.get(word1)
        index2s = d.get(word2)
        result = len(words)
        # 双重循序计算索引差值
        for index1 in index1s:
            for index2 in index2s:
                if abs(index1 - index2) < result:
                    result = abs(index1 - index2)
        return result


if __name__ == "__main__":
    words =  ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "makes"
    word2 = "coding"
    answer = Solution().shortestDistance(words, word1, word2)
    print(answer)