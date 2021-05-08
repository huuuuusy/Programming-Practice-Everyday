""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    改变思路，不使用额外空间，直接分析每一列的变化规律进行构建
结果：
    执行用时 : 40 ms, 在所有 Python3 提交中击败了97.84%的用户
    内存消耗 : 13 MB, 在所有 Python3 提交中击败了87.70%的用户
"""

class Solution:
    def getRow(self, rowIndex):
        result = [1, 1]
        # 排除特殊情况
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return result
        # 对于一般情况，先在每行前面添加１，然后将当前元素和后一个元素求和后进行替换
        for i in range(2, rowIndex+1):
            result.insert(0, 1)
            for i in range(1, i):
                result[i] = result[i] + result[i+1]
        return result
        
if __name__ == "__main__":
    nums = 5
    answer = Solution().getRow(nums)
    print(answer)
        



