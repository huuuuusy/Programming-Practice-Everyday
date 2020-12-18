""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    用字典存储下标，然后检查下标之间的最小差值是否不超过k
    时间空间复杂度不行，可以考虑双指针＋滑动窗口优化
结果：
    执行用时 : 56 ms, 在所有 Python3 提交中击败了88.87%的用户
    内存消耗 : 17.7 MB, 在所有 Python3 提交中击败了92.72%的用户
"""

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        if n <= 1:
            return False
        # record记录数组里的k个数,为窗口大小
        record = set()
        for i in range(n):
            # 数组中已经存有nums[i],说明窗口大小不大于k
            if nums[i] in record:
                return True
            # 否则添加nums[i]
            record.add(nums[i])
            # 当窗口大于k时,移除第一个元素
            if len(record) > k:
                record.remove(nums[i-k])
        return False


if __name__ == "__main__":
    nums = [1,2,3,1]
    k = 3
    answer = Solution().containsNearbyDuplicate(nums, k)
    print(answer)