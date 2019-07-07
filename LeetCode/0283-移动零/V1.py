""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    循环判断，是0则删除并在最后添加0，非0则保留
    j作为指针指向已经检查完的非0元素的末尾
结果：
    执行用时 : 64 ms, 在所有 Python3 提交中击败了87.96%的用户
    内存消耗 : 14.3 MB, 在所有 Python3 提交中击败了90.01%的用户
"""

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[j] == 0:
                nums.pop(j)
                nums.append(0)
            else:
                j += 1
        return nums

if __name__ == "__main__":
    nums = [0,0,1]
    answer = Solution().moveZeroes(nums)
    print(answer)