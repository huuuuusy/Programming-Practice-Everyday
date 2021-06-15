"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] == 0:
                count += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        # 最后将空余位置置0
        for i in range(count):
            nums[-(i+1)] = 0
        return nums

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    answer = Solution().moveZeroes(nums)
    print(answer)
