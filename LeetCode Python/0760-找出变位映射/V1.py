""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    使用哈希表存储元素，然后再检查
注意：
    注意重复数字在字典中的存储方式
结果：
    执行用时 : 68 ms, 在所有 Python3 提交中击败了35.80%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def anagramMappings(self, A, B):
        res = []
        d = {}
        # 此处存储数组而不是直接存index,是为了解决重复数字的情况
        for index, value in enumerate(B):
            d[value] = d.get(value, []) + [index]
        for num in A:
            res.append(d[num][0])
        return res




if __name__ == "__main__":
    A = [21,5,74,5,74,21]
    B = [21,5,74,74,5,21]
    answer = Solution().anagramMappings(A, B)
    print(answer)