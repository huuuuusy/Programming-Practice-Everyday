""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    简单题
结果：
    执行用时 : 352 ms, 在所有 Python3 提交中击败了86.82%的用户
    内存消耗 : 15.1 MB, 在所有 Python3 提交中击败了41.60%的用户
"""

class Solution:
    def majorityElement(self, nums):
        for num in set(nums):
            if nums.count(num) > len(nums)//2:
                return num
        

if __name__ == "__main__":
    nums = [3,2,3]
    answer = Solution().majorityElement(nums)
    print(answer)