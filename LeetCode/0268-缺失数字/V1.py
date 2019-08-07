""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    直接用循环会超时，用哈希表后不超时但是时间复杂度可以进一步提升
结果：
    执行用时 : 192 ms, 在所有 Python3 提交中击败了20.82%的用户
    内存消耗 : 15.7 MB, 在所有 Python3 提交中击败了5.36%的用户
"""

class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    answer = Solution().missingNumber(nums)
    print(answer)