"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2

解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 
提示：
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()

        # 初始化
        a = abs(nums[0] + nums[1] + nums[2] - target) # 存储最开始三个元素和target的距离
        res = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # 只需要多一步更新阈值并存储结果的环节
                if abs(total - target) < a:
                    # 此时距离小于当前阈值,更新阈值
                    a = abs(total - target)
                    res = total

                # 双指针
                if total == target:
                    return total
                elif total > target:
                    right -= 1
                elif total < target:
                    left += 1
        return res


if __name__ == "__main__":
    nums = [0,0,0]
    target = 1
    answer = Solution().threeSumClosest(nums, target)
    print(answer)