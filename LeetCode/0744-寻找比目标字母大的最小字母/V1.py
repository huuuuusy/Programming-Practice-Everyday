""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    二分查找
结果：
    执行用时 : 156 ms, 在所有 Python3 提交中击败了35.38%的用户
    内存消耗 : 14.1 MB, 在所有 Python3 提交中击败了5.41%的用户
"""

class Solution:
    def nextGreatestLetter(self, letters, target):
        # 循环字母，所以先排除特殊情况
        if target >= letters[-1]:
            return letters[0]
        # 二分查找
        left = 0
        right = len(letters) - 1 
        while left < right:
            # 左中位数
            mid = (left + right) >> 1 
            if letters[mid] <= target:
                left = mid + 1 # 左边界收缩
            else:
                right = mid
        return letters[left]
 
if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "j"
    answer = Solution().nextGreatestLetter(letters, target)
    print(answer)