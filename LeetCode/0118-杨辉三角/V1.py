""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    排除特殊情况后直接按照杨辉三角形的规律构建
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了74.69%的用户
    内存消耗 : 13 MB, 在所有 Python3 提交中击败了94.55%的用户
"""

class Solution:
    def generate(self, numRows):
        list_1 = [1]
        list_2 = [1, 1]
        result = []
        # 排除３种特殊情况
        if numRows == 0:
            return result
        if numRows == 1:
            result.append(list_1)
            return result
        if numRows == 2:
            result.append(list_1)
            result.append(list_2)
            return result
        # 一般情况
        result.append(list_1)
        result.append(list_2)
        for i in range(3, numRows+1):
            # 新建一行全１列表
            list_i = [1 for _ in range(i)]
            # 读取上一行列表
            list_previous_i = result[i-2]
            # 替换元素
            for j in range(1, i-1):
                list_i[j] = list_previous_i[j-1] + list_previous_i[j]
            result.append(list_i)
        return result


if __name__ == "__main__":
    nums = 5
    answer = Solution().generate(nums)
    print(answer)
        