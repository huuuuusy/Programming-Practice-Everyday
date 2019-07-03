""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
"""

"""
一轮循环:
    在列表中循环查找target－current_num
    如果存在，则返回两个数字的下标
注意:
    second_index要在remain_nums中查，然后加上之前的数字
    直接在nums中查找，会无法通过两个数字相同的测试
    eg. nums = [3,3], target = 6, answer = [0,1]
        为了不返回[0,0],需要在remain_nums中计算second_index
结果：
    执行用时 : 852 ms, 在所有 Python 提交中击败了49.32%的用户
    内存消耗 : 12.7 MB, 在所有 Python 提交中击败了25.75%的用户
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for first_index in range(0, len(nums)):
            second_num = target - nums[first_index]
            remain_nums = nums[first_index + 1:]
            if second_num in remain_nums:
                second_index = remain_nums.index(second_num) + first_index + 1
                result.append([first_index, second_index])
                break
        return result[0]
                
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    answer = Solution().twoSum(nums, target)
    print(answer)