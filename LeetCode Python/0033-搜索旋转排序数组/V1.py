""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路：
    调包......
结果：
    执行用时 : 68 ms, 在所有 Python3 提交中击败了31.12%的用户
    内存消耗 : 14.1 MB, 在所有 Python3 提交中击败了5.73%的用户
"""

class Solution:
    def search(self, nums, target):
        return nums.index(target) if target in nums else -1

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    answer = Solution().search(nums, target)
    print(answer)