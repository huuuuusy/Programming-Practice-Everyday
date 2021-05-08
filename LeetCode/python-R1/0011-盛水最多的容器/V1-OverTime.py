""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
"""

"""
两轮循环:
    暴力解法，直接计算所有状态进行比价
结果：
    在第42个测试用例超出时间范围
"""

class Solution:
    def maxArea(self, height):
        max = 0
        for i in range(0, len(height)):
            for j in range(i+1, len(height)):
                if height[i] < height[j]:
                    tall = height[i]
                else:
                    tall = height[j]
                area = tall * (j-i)
                if area >= max:
                    max = area
        return max



if __name__ == "__main__":
    nums = [1,1]
    answer = Solution().maxArea(nums)
    print(answer)
