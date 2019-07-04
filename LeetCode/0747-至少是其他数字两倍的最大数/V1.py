""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    先排除几种特殊情况，然后将数组变为2倍
    新数组中第二大的数字和原数组最大的数字比较，得到结果
注意：
    需要分析清楚特殊情况的返回值
结果：
    执行用时 : 52 ms, 在所有 Python 提交中击败了77.80%的用户
    内存消耗 : 13 MB, 在所有 Python 提交中击败了93.97%的用户
"""

class Solution:
    def dominantIndex(self, nums):
        # 排除特殊数组
        if len(nums) == 0:
            return -1
        if len(nums) == 1 and (nums[0] == 0 or nums[0] == 1):
            return 0
        # 对一般的输入，直接比较即可
        max_num = max(nums)
        double_nums = [x*2 for x in nums]
        double_nums.sort()
        target = double_nums[-2]
        if max_num < target:
            return -1
        else:
            return nums.index(max_num)



if __name__ == "__main__":
    nums =  [3, 6, 1, 0]
    answer = Solution().dominantIndex(nums)
    print(answer)