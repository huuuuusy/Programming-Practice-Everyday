""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    经典的二分查找题，需要仔细理解二分查找的细节点，参考链接讲解的很清晰
参考链接：
    https://leetcode-cn.com/problems/binary-search/solution/er-fen-cha-zhao-xiang-jie-by-labuladong/
结果：
    执行用时 : 364 ms, 在所有 Python3 提交中击败了34.1%的用户
    内存消耗 : 15.1 MB, 在所有 Python3 提交中击败了5.20%的用户
"""

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1 # right是搜索区域的最右边的坐标，为列表长度-1 
        while left <= right: # left <= right是为了保证left=right时的元素也可以被检索
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] >  target:
                right = mid - 1
        return -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    answer = Solution().search(nums, target)
    print(answer)