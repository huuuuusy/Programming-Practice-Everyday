""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
"""

"""
字典：
    利用字典存储数字－序号作为键－值对
    第一个数字被存入字典
    当第二个数字被循环到后，会在字典中读出第一个数字的信息
    最后返回两个数字的序号
注意:
    nums_dict[nums[i]] = i应放到循环的最后
    eg. nums = [3,2,4], target=6
        如果放到循环的最前，则会返回[0,0]而非[1,2]
结果：
    执行用时 : 76 ms, 在所有 Python 提交中击败了61.21%的用户
    内存消耗 : 13.2 MB, 在所有 Python 提交中击败了6.84%的用户
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i in range(0, len(nums)):
            second_num = target - nums[i]
            if second_num in nums_dict:
                return [nums_dict[second_num], i]
            nums_dict[nums[i]] = i
        
                
if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    answer = Solution().twoSum(nums, target)
    print(answer)