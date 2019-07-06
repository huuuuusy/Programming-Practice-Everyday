""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    滑动窗口
    左右指针确定滑动窗口大小
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了98.71%的用户
    内存消耗 : 14.2 MB, 在所有 Python3 提交中击败了99.21%的用户
"""

class Solution:
    def minSubArrayLen(self, s, nums):
        if sum(nums) < s:
            return 0
        if sum(nums) == s:
            return len(nums)
        left = 0
        right = 0
        sub_sum = 0
        length = len(nums)
        for right, item in enumerate(nums):
            sub_sum += item
            while sub_sum >= s:
                length = min(length, right - left + 1)
                sub_sum -= nums[left]
                left += 1
        return length


if __name__ == "__main__":
    s = 7
    nums = [2,3,1,2,4,3]
    answer = Solution().minSubArrayLen(s, nums)
    print(answer)