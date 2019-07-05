""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    先排序，再两两一组进行计算
结果：
    执行用时 : 188 ms, 在所有 Python3 提交中击败了20.18%的用户
    内存消耗 : 14.9 MB, 在所有 Python3 提交中击败了81.23%的用户
"""

class Solution:
    def arrayPairSum(self, nums):
        if len(nums) == 0:
            return 0
        nums.sort()
        result = 0
        i = 0
        while i < int(len(nums)/2):
            result += min(nums[2*i], nums[2*i+1])
            ｉ += 1
        return result
      
if __name__ == "__main__":
    nums = [7,3,1,0,0,6]
    answer = Solution().arrayPairSum(nums)
    print(answer)