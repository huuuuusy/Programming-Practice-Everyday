""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    可以分为以下两种情况：
        1、中间数与左边界比较:
            尝试在纸上写出几个例子：
            例 1：[1, 2, 3, 4, 5]
            例 2：[2, 3, 4, 5, 1]
            以上这两个例子，中间数都比左边界大，
            但是旋转排序数组的最小值可能在中间数的左边（例 1），也可能在中间数的右边（例 2），
            因此不能使用中间数与左边界比较作为二分法的讨论依据。
        2、中间数与右边界比较：
            （1）当中间数比右边界表示的数大的时候，中间数就一定不是目标数（旋转排序数组的最小值）。
                例 3：[7, 8, 9, 10, 11, 12, 1, 2, 3]
                中间数 11 比右边界 3 大，因此中间数以及中间数前面的数都不是目标数，
                把左边界设置中间数位置 + 1，即 left = mid + 1；
            （2）当中间数比右边界表示的数小的时候，中间数就可能是目标数（旋转排序数组的最小值）：
                例 4：[7, 8, 1, 2, 3]
                中间数 1 比右边界表示的数小的时候，说明中间数到右边界是递增的（对于这道题是非递减），
                那么中间数右边的（不包括中间数）就一定不是目标数，可以把它们排除，
                不过中间数有可能是目标数，就如本例，因此，把右边界设置为 right = mid。
            （3）当中间数与右边界表示的数相等的时候，看下面两个例子：
                例 5：[0, 1, 1, 1, 1, 1, 1]
                例 6：[1, 1, 1, 1, 0, 1, 1]
                目标值可能在中间数的左边，也可能在中间数的右边，
                此时你看到的是右边界，就把只右边界排除掉就好了。
                正是因为右边界和中间数相等，你去掉了右边界，中间数还在，就让中间数在后面的循环中被发现吧。
            因此，根据中间数和右边界的大小关系，可以使用二分法搜索到目标值。
参考：
    https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/solution/er-fen-fa-fen-zhi-fa-python-dai-ma-by-liweiwei1419/
结果：
    执行用时 : 72 ms, 在所有 Python3 提交中击败了45.70%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了5.75%的用户
"""

class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums)-1 
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1 # 左边界收缩
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1 
        return nums[left]

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    answer = Solution().findMin(nums)
    print(answer)