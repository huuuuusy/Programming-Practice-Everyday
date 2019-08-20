""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路：
    双指针
    第一个指针负责遍历所有元素，当前元素等于目标值则跳过，不等于目标值则将其复制到第二个指针的位置
    然后第二个指针向后移动一位，其最终位置即为非目标元素的个数
结果：
    执行用时 : 44 ms, 在所有 Python3 提交中击败了96.19%的用户
    内存消耗 : 13.1 MB, 在所有 Python3 提交中击败了67.95%的用户
"""

class Solution:
    def removeElement(self, nums, val):
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    answer = Solution().removeElement(nums, val)
    print(answer)