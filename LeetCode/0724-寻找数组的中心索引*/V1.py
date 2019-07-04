""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    两轮循环，暴力解法
    从左到右遍历数组,left[i]存储i左边所有元素的和
    然后再次循环，计算出右边元素之和，然后和左边元素比较，判断返回值
结果：
    执行用时 : 84 ms, 在所有 Python3 提交中击败了52.61%的用户
    内存消耗 : 14 MB, 在所有 Python3 提交中击败了88.38%的用户
"""

class Solution:
    def pivotIndex(self, nums):
        left = []
        sum = 0
        # 对每个元素，计算其左边元素的和，然后存入列表
        for num in nums:
            sum += num
            left.append(sum - num)
        # 计算右边元素的和，与左边元素比较
        for i in range(len(nums)):
            left_sum = left[i]
            rigth_sum = sum - left_sum - nums[i]
            if left_sum == rigth_sum:
                return i
        return -1

if __name__ == "__main__":
    nums =  [1, 7, 3, 6, 5, 6]
    answer = Solution().pivotIndex(nums)
    print(answer)
        