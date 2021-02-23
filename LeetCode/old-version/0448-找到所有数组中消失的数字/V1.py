""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    和268题目的思路一致，用集合存储数字，然后检索
结果：
    执行用时 : 500 ms, 在所有 Python3 提交中击败了23.87%的用户
    内存消耗 : 23.8 MB, 在所有 Python3 提交中击败了5.06%的用户
"""

class Solution:
    def findDisappearedNumbers(self, nums):
        new_nums = set(nums)
        result = []
        for i in range(1,len(nums)+1):
            if i not in new_nums:
                result.append(i)
        return result


if __name__ == "__main__":
    nums = [1,1]
    answer = Solution().findDisappearedNumbers(nums)
    print(answer)
