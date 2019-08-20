""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    双指针
    不断移动左右指针，读取连续1的长度
    执行速度有点慢
结果：
    执行用时 : 184 ms, 在所有 Python3 提交中击败了14.36%的用户
    内存消耗 : 13.3 MB, 在所有 Python3 提交中击败了59.9%的用户
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        left = 0
        right = 0
        # start表示开始进入连续1
        start = True
        result = []
        while right < len(nums): 
            # 如果开始连续1，则固定left，移动right
            if start:
                while nums[right] == 1:
                    right += 1
                    if right >= len(nums):
                        break
                result.append(right - left)
                left = right
                start = False
            # 如果停止连续1，则固定right，移动left
            else:
                while nums[left] != 1:
                    left += 1
                    if left >= len(nums):
                        break
                right = left
                start = True
        return max(result)


if __name__ == "__main__":
    nums = [1,1,0,1,1,1]
    answer = Solution().findMaxConsecutiveOnes(nums)
    print(answer)