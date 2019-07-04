""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    一轮循环
    对于左边的和，每次通过循环叠加即可得到
    对于右边的和，每次通过循环从总和中减去当前数字即可得到
注意：
    左侧的和与右侧的和在循环中更新的位置不同
结果：
    执行用时 : 76 ms, 在所有 Python3 提交中击败了83.62%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了94.19%的用户
"""

class Solution:
    def pivotIndex(self, nums):
        left = 0
        right = sum(nums)
        # 注意right和left在循环中的位置
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1

if __name__ == "__main__":
    nums =  [1, 7, 3, 6, 5, 6]
    answer = Solution().pivotIndex(nums)
    print(answer)
        