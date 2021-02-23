""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
"""

"""
一轮循环:
    直接判断target和列表中每个数字的关系，从而确定插入位置
注意：
    注意不要遗漏target比列表所有数字大的情况
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了89.48%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了58.54%的用户
"""

class Solution:
    def searchInsert(self, nums, target):
        for i in range(0, len(nums)):
            if target < nums[i]:
                nums.insert(i, target)
                return i 
            elif target == nums[i]:
                return i
            else:
                continue
        nums.insert(i+1, target)
        return i+1

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 5
    answer = Solution().searchInsert(nums,target)
    print(answer)
