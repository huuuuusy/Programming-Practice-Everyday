""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.39
工具： python == 3.7.3
"""

"""
思路:
    滑动窗口
结果：
    执行用时 : 1320 ms, 在所有 Python3 提交中击败了38.54%的用户
    内存消耗 : 17.4 MB, 在所有 Python3 提交中击败了5.79%的用户
"""

class Solution:
    def findMaxAverage(self, nums, k):
        res = _sum = sum(nums[0:k]) # 初始时的连续数的和
        for i in range(k, len(nums)):
            _sum += nums[i] - nums[i-k] # 滑动窗口
            res = max(res, _sum) # 保留最大值
        return res / k


if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    answer = Solution().findMaxAverage(nums, k)
    print(answer)