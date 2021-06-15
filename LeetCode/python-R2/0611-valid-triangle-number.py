"""
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:
输入: [2,2,3,4]
输出: 3

解释:
有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3

注意:
数组长度不超过1000。
数组里整数的范围为 [0, 1000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-triangle-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
类似于0015的三数之和
固定第一个数字，双指针判断后面数字两数之和是否大于第三个数
注意此处双指针和固定数字的设置：固定数字从第三个数字开始，双指针在左边的列表滑动
"""
class Solution:
    def triangleNumber(self, nums):
        count = 0 
        nums.sort()

        for i in range(2, len(nums)):
            left, right = 0, i-1
            while left < right:
                if nums[left]+nums[right] > nums[i]:
                    # 这些都可以：[left,right]、[left+1,right]...[right-1,right]
                    count += right-left
                    right -= 1
                else:
                    left += 1
        return count

if __name__ == "__main__":
    nums = [2,2,3,4]
    answer = Solution().triangleNumber(nums)
    print(answer)