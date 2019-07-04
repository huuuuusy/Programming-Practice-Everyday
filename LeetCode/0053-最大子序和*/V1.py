""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
"""

"""
思路:
    暴力解法
    把之前的序列看做一个整体，如果整体呈正数则保留，整体呈非正数则替换
注意:
    else部分需要仍然比较当前数字和max_num的关系，如果当前数字大，需要做替换（这种情况容易遗漏)
结果：
    执行用时 : 60 ms, 在所有 Python 提交中击败了82.30%的用户
    内存消耗 : 13.4 MB, 在所有 Python 提交中击败了96.67%的用户
"""

class Solution:
    def maxSubArray(self, nums):
        sum = nums[0]
        max_num = sum
        for i in range(1, len(nums)):
            # sum是当前数字左侧数字的和
            # 如果这个和大于0，说明之前的序列整体呈现一个正数，可以作为最终序列的一部分保留
            if sum > 0:
                sum = sum + nums[i]
                # 此时比较当前最大子序和与sum
                # 如果超过当前最优结果，则替换
                max_num = max(max_num, sum)
            else:
                # sum小于0,说明之前整体呈现0或者负数，应舍弃，从当前数字开始重新计算sum
                # 此时应该仍然比较一下max_num和当前数字的关系，如果当前数字大，则替换max_num
                max_num = max(max_num, nums[i])
                sum = nums[i]
        return max_num

if __name__ == "__main__":
    nums =  [-2,1]
    answer = Solution().maxSubArray(nums)
    print(answer)
        