""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
"""

"""
双指针：
    在列表的左右各放一个指针，先保证宽度（两个指针的距离）尽可能大
    然后再移动较低的指针，尽可能使较高的指针保持和其他值之间距离最大
结果：
    执行用时 : 176 ms, 在所有 Python3 提交中击败了5.50%的用户
    内存消耗 : 14 MB, 在所有 Python3 提交中击败了99.38%的用户
"""

class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        area = 0
        
        while left < right:
            cur = min(height[left], height[right]) * (right - left)
            area = max(area, cur)
            # 较短的垂直线往中间移动
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area     

if __name__ == "__main__":
    nums = [1,1]
    answer = Solution().maxArea(nums)
    print(answer)
