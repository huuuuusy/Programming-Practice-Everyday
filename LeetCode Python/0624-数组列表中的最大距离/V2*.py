""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    单轮循环，借助排序数组的特性，利用start和end维护当前的最小值和最大值
结果：
    执行用时 : 200 ms, 在所有 Python3 提交中击败了87.50%的用户
    内存消耗 : 16.8 MB, 在所有 Python3 提交中击败了100.00%的用户
"""

class Solution:
    def maxDistance(self, arrays):
        res = float("-inf")
        # 排序数组，start和end直接按位置读取即可
        start = arrays[0][0] 
        end = arrays[0][-1]
        for i in range(1, len(arrays)):
            res = max(res, abs(start - arrays[i][-1]), abs(end - arrays[i][0])) # res存储当前最大差值
            start = min(start, arrays[i][0]) # start始终存储当前最小的元素
            end = max(end, arrays[i][-1]) # end始终存储当前最大的元素
        return res




if __name__ == "__main__":
    arrays = [[1,2,3],[4,5],[1,2,3]]
    answer = Solution().maxDistance(arrays)
    print(answer)