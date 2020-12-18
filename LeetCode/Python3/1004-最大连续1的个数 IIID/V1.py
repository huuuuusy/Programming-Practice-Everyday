""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    滑动窗口
结果：
    执行用时 : 252 ms, 在所有 Python3 提交中击败了69.39%的用户
    内存消耗 : 13.4 MB, 在所有 Python3 提交中击败了92.94%的用户
"""

class Solution:
    def longestOnes(self, A, K):
        # max_ones记录连续1最多有多少
        # zero_count记录已经转换的0
        # left和right是滑动窗口的指针
        max_ones = 0
        zero_count = 0
        left = 0
        right = 0
        for right, item in enumerate(A):
            # 当前元素为0则zero_count + 1
            if item == 0:
                zero_count += 1
            # 当已经使用k个0时
            # 判断窗口左边是否可以移动
            while zero_count > K:
                if A[left] == 0:
                    zero_count -= 1
                left += 1
            # 记录当前最大窗口
            max_ones = max(max_ones, right - left + 1)
        return max(max_ones, right - left + 1)


if __name__ == "__main__":
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    K = 3
    answer = Solution().longestOnes(nums, K)
    print(answer)