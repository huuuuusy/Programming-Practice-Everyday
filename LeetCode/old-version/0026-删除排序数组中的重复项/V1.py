""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
"""

"""
一轮循环:
    在列表中直接倒序查找当前数字和前一数字是否相同
    相同则删除
注意：
    不允许创建新的列表，需要直接对当前列表进行操作
结果：
    执行用时 : 112 ms, 在所有 Python3 提交中击败了37.70%的用户
    内存消耗 : 114.6 MB, 在所有 Python3 提交中击败了97.41%的用户
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]: 
                nums.pop(i)
        return len(nums)

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    answer = Solution().removeDuplicates(nums)
    print(answer)
