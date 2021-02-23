""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    动态规划
    dp1: 允许进行0转1操作，连续1的个数
    dp0: 不允许进行0转1操作，连续1的个数
    num=0:
        dp1 = dp0 +1 未进行0转1时连续1的个数加上转换后的1
        dp0 = 0 置0，重新开始统计
    num=1:
        dp1 += 1 
        dp0 += 1
注意　：
    在num=0时，先更新dp1，再重置dp0
结果：
    执行用时 : 172 ms, 在所有 Python3 提交中击败了100%的用户
    内存消耗 : 13 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        dp0 = 0
        dp1 = 0
        result = 0
        for num in nums:
            if num == 0:
                dp1 = dp0 + 1
                dp0 = 0
            else:
                dp1 += 1
                dp0 += 1
            result = max(result, dp0, dp1)
        return result


if __name__ == "__main__":
    nums = [1,1,1,0,0,1,1,0,1]
    answer = Solution().findMaxConsecutiveOnes(nums)
    print(answer)