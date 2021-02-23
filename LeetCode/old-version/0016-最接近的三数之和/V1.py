""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.39
工具： python == 3.7.3
"""

"""
思路:
    双指针
结果：
    执行用时 : 124 ms, 在所有 Python3 提交中击败了88.13%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.04%的用户
"""

class Solution:
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        n = len(nums)
        res = float('inf')
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]: # 如果当前数值已经出现，则直接跳过本次循环
                continue
            left = i+1
            right = n-1
            while left < right:
                cur = nums[left] + nums[right] + nums[i] # 计算当前结果　
                if cur == target: # 如果当前数值等于target则直接返回
                    return target
                if abs(cur - target) < abs(res - target): # 如果与target的差距缩小，则进行替换
                    res = cur
                if cur > target: # 如果当前值偏大，则右指针左移
                    right -= 1 
                if cur < target: # 如果当前值偏小，则左指针右移
                    left += 1
        return res

if __name__ == "__main__":
    nums = [0,2,1,-3]
    target = 1
    answer = Solution().threeSumClosest(nums, target)
    print(answer)

