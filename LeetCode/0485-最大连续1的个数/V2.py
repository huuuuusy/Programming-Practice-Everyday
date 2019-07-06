""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    遍历所有数字
    是1则计数加一，否则计数置0
结果：
    执行用时 : 128 ms, 在所有 Python3 提交中击败了51.52%的用户
    内存消耗 : 13.1 MB, 在所有 Python3 提交中击败了97.17%的用户
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_one = 0
        count_one = 0
        for num in nums:
            if num == 1:
                count_one += 1
                max_one = max(max_one, count_one)
            else:
                count_one = 0
        return max(max_one, count_one)


if __name__ == "__main__":
    nums = [1,1,0,1,1,1]
    answer = Solution().findMaxConsecutiveOnes(nums)
    print(answer)