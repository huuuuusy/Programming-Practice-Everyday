""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    用set()函数排除重复元素
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了94.57%的用户
    内存消耗 : 18.6 MB, 在所有 Python3 提交中击败了83.08%的用户
"""

class Solution:
    def containsDuplicate(self, nums):
        if len(set(nums)) != len(nums):
            return True
        else:
            return False

if __name__ == "__main__":
    nums = [1,1,1,3,3,4,3,2,4,2]
    answer = Solution().containsDuplicate(nums)
    print(answer)