""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37.1
工具： python == 3.7.3
"""

"""
思路:
    使用哈希表
结果：
    执行用时 : 64 ms, 在所有 Python3 提交中击败了47.23%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def isMajorityElement(self, nums, target):
        # 排除特殊情况
        if len(nums) == 1:
            return True if nums[0] == target else False
        if len(nums) == 0:
            return False
        # 用哈希表记录，然后判断是否满足条件
        d = {} 
        for index, value in enumerate(nums):
            d[value] = d.get(value,0) + 1
        return True if max(d.values()) > len(nums)/2 else False

if __name__ == "__main__":
    nums = [438885258]
    target = 786460391
    answer = Solution().isMajorityElement(nums, target)
    print(answer)