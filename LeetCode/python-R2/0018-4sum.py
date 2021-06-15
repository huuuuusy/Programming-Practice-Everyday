"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：答案中不可以包含重复的四元组。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
输入：nums = [], target = 0
输出：[]

提示：
0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        
        if len(nums) < 4:
            return res
        
        # 前两个数字用双重循环
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                
                # 剪枝
                if nums[i] + nums[j] + nums[j+1] +nums[j+2] > target:
                    continue
                if nums[i] + nums[j] + nums[-2] + nums[-1] < target:
                    continue

                left, right = j+1, len(nums)-1
                
                # 双指针
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        if [nums[i], nums[j], nums[left], nums[right]] not in res:
                            res.append([nums[i], nums[j], nums[left], nums[right]])
                        if nums[left+1] == nums[left]:
                            left += 1
                        if nums[right-1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1                    
        return res


if __name__ == "__main__":
    nums = [2,2,2,2]
    target = 8
    answer = Solution().fourSum(nums, target)
    print(answer)