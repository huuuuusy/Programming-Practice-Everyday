""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
"""

"""
双指针:
    先在大循环里确定第一个数字
    然后从下一个数字起使用双指针从两端进行移到
    判断三个数字的和是否为0
注意:
    最开始先排序，如果第一个元素>0，则可以直接跳出循环-->节约时间
    注意判断当前数字和下一个数字是否相同，如果相同则跳过，否则结果会重复
结果：
    执行用时 : 860 ms, 在所有 Python 提交中击败了90.89%的用户
    内存消耗 : 16.8 MB, 在所有 Python 提交中击败了53.94%的用户
"""

class Solution:
    def threeSum(self, nums):
        # 先对nums进行排序
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):

            # 如果排序后的列表第一个数字大于０，说明列表所有元素大于０
            # 此情况没有符合题意的结果，直接退出循环
            if nums[i] > 0:
                break
            
            # 如果前一个数字和当前数字相同，则跳过本次循环
            # 否则将输出相同的结果
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            # 使用双指针进行排序
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                # 如果当前的三个值的和为０，则保存结果，并且left和right均移到下一个位置
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # 讨论两种特殊情况：
                    # 和上面的当前数字需要判断是否与前一数字相同的情况类似
                    # 如果left和right下一个移动目标和当前目标相同，则跳过
                    # 否则将输出相同的结果
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    
                    left += 1
                    right -= 1

                # 如果当前的和小于0，说明应该移动left，使和增大
                elif sum < 0:
                    left += 1

                # 如果当前的和大于0,说明应该移动right,使和减小
                else:
                    right -= 1
        
        return result

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    answer = Solution().threeSum(nums)
    print(answer)

