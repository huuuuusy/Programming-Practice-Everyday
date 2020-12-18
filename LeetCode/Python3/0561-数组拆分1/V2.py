""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    先排序
    对排序结果，第0,2,4,...个元素是每对的最小值
    利用切片提取结果，然后求和即可
结果：
    执行用时 : 128 ms, 在所有 Python3 提交中击败了88.15%的用户
    内存消耗 : 15 MB, 在所有 Python3 提交中击败了56.00%的用户
"""

class Solution:
    def arrayPairSum(self, nums):
        result = sum(sorted(nums)[::2])
        return result
      
if __name__ == "__main__":
    nums = [7,3,1,0,0,6]
    answer = Solution().arrayPairSum(nums)
    print(answer)