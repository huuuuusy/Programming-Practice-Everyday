"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]
 
提示：
0 <= nums.length <= 3000
-105 <= nums[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
解法：
    排序
    从最左边开始依次固定一个数字
    从固定数字右侧数组开始解两数之和
"""

# 双指针
class Solution:
    def threeSum(self, nums):
        nums.sort() # 排序
        res = []

        if len(nums) < 3:
            return res
        
        for i in range(len(nums)-2): 
            first = nums[i] # 固定的数字
            if first + nums[-1] + nums[-2] < 0: 
                # 如果固定的数字加上数组中最大的两个数字后依旧小于0，说明固定的数字太小
                continue
            elif first + nums[i+1] + nums[i+2] > 0: 
                # 如果当前最小的三个数字之和大于0，说明没必要再检查了，退出外层循环
                break

            # 两数之和
            left, right = i+1, len(nums)-1
            while left < right:
                total = first + nums[left] + nums[right]
                if total == 0:
                    if [first, nums[left], nums[right]] not in res:
                        res.append([first, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res


"""
优化：
    注意存在重复元素，排序后重复元素可以跳过
"""
# 优化
class Solution1:
    def threeSum1(self, nums):
        nums.sort() # 排序
        res = []

        if len(nums) < 3:
            return res
        
        for i in range(len(nums)): 
            first = nums[i] # 固定的数字
            if i > 0 and nums[i] == nums[i-1]:
                # 去重
                continue

            # 两数之和
            left, right = i+1, len(nums)-1
            while left < right:
                total = first + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                elif total == 0:
                    res.append([first, nums[left], nums[right]])
                    # 去重（如果当前数和相邻的数相等，直接移动指针）
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                
        return res


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    answer = Solution().threeSum(nums)
    print(answer)