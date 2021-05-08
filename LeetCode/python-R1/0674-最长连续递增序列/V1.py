""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.39
工具： python == 3.7.4
"""

"""
思路:
    二分查找
结果：
    执行用时 : 80 ms, 在所有 Python3 提交中击败了98.66%的用户
    内存消耗 : 14 MB, 在所有 Python3 提交中击败了79.4%的用户
"""

class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        maxCount, count = 1, 1
        for i in range(len(nums) - 1):
                # 处于递增中
            if nums[i + 1] > nums[i]:
                count += 1
            else:
                # 计算最大长度
                maxCount = max(maxCount, count)
                count = 1
        # 最大长度在数组末尾的情况
        return max(maxCount, count)


if __name__ == "__main__":
    nums = [2,2,2,2,2]
    answer = Solution().findLengthOfLCIS(nums)
    print(answer)
            
        