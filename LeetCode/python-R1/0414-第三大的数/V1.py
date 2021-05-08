""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    二分查找
结果：
    执行用时 : 84 ms, 在所有 Python3 提交中击败了47.41%的用户
    内存消耗 : 15.1 MB, 在所有 Python3 提交中击败了5.41%的用户
"""

class Solution:
    def thirdMax(self, nums):
        return sorted(set(nums))[-3] if len(set(nums)) >= 3 else max(nums)

            

if __name__ == "__main__":
    nums = [3, 2, 1]
    answer = Solution().thirdMax(nums)
    print(answer)
