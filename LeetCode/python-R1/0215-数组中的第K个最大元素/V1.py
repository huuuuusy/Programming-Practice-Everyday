""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    python大法好
结果：
    执行用时 : 88 ms, 在所有 Python3 提交中击败了63.04%的用户
    内存消耗 : 14.6 MB, 在所有 Python3 提交中击败了19.21%的用户
"""

class Solution:
    def findKthLargest(self, nums, k):
        return sorted(nums)[-k]

if __name__ == "__main__":
    k = 2
    nums = [3,2,1,5,6,4]
    answer = Solution().findKthLargest(nums, k)
    print(answer)