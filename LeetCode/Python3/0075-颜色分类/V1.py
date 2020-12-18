""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    计数＋替换
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了83.11%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.21%的用户
"""

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums_0和nums_1分别统计原列表中0和1的个数
        num_0 = 0
        num_1 = 0
        for num in nums:
            if num == 0:
                num_0 += 1
            elif num == 1:
                num_1 += 1
        # 将原数组中的元素依次进行替换
        for s in range(0,num_0):
            nums[s] = 0
        for s in range(num_0, num_0 + num_1):
            nums[s] = 1
        for s in range(num_0 + num_1, len(nums)):
            nums[s] = 2
        return nums

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    answer = Solution().sortColors(nums)
    print(answer)