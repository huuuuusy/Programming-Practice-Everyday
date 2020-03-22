""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.40
工具： python == 3.7.3
"""

"""
思路:
    贪心算法
参考：
    https://leetcode-cn.com/problems/non-decreasing-array/solution/665-fei-di-jian-shu-lie-tan-xin-pan-duan-9947-by-t/
结果：
    执行用时 : 320 ms, 在所有 Python3 提交中击败了19.63%的用户
    内存消耗 : 14.9 MB, 在所有 Python3 提交中击败了5.43%的用户
"""

class Solution:
    def checkPossibility(self, nums):
        flag = True
        nums += [10000, 0]
        for i in range(len(nums) - 2):
            if nums[i] > nums[i + 1]:
                if not flag:
                    return False
                if nums[i + 1] < nums[i - 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                flag = False
        return True

if __name__ == "__main__":
    nums = [3,3,2,2]
    answer = Solution().checkPossibility(nums)
    print(answer)
            
        