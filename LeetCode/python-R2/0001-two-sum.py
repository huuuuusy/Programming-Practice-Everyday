"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
 
提示：
2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


#哈希解法
class Solution:
    def twoSum(self, nums, target):
        map = {} # 创立一个哈希表
        for i in range(len(nums)):
            if target- nums[i] in map:
                # 如果哈希表中存在目标元素
                return map[target-nums[i]], i
            else:
                # 将元素存入哈希表中，键为元素，值为元素在数组中的坐标
                map[nums[i]] = i 

# 双指针
class Solution:
    def twoSum(self, nums, target):
        array = nums.copy() # 复制原始数组
        nums.sort() # 双指针使用前需要排序
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                break
        
        # 将返回值恢复为原始数组的索引
        res = []
        for i in range(len(array)):
            if array[i] == nums[left] or array[i] ==  nums[right]:
                res.append(i)
        return res


