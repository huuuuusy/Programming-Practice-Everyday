""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    二分查找+贪心算法
参考链接：
    https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
结果：
    执行用时 : 80 ms, 在所有 Python3 提交中击败了76.14%的用户
    内存消耗 : 14 MB, 在所有 Python3 提交中击败了5.31%的用户
"""

class Solution:
    def lengthOfLIS(self, nums):
        l = len(nums)
        if l < 2: 
            return l
        tail = [nums[0]] # tail是存储最长序列的list
        for i in range(1, l):
            # 如果当前元素值大于tail中最大的元素，则直接将其添加到tail的末尾
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue
            # 使用二分查找，确定tail中大于等于nums[i]的元素的位置
            left = 0 
            right = len(tail) - 1 
            while left < right:
                mid = (left + right) >> 1 # 使用左中位数，因为后面左边界收缩
                if tail[mid] < nums[i]:
                    left = mid + 1 # 左边界收缩
                else:
                    right = mid 
            tail[left] = nums[i]
        return len(tail)


if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    answer = Solution().lengthOfLIS(nums)
    print(answer)