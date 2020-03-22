""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    直接将每个数字从0开始到自己的和存入target数组中
    最后返回两个数字在target数组的差值即为结果
参考链接：
    https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
结果：
    执行用时 : 104 ms, 在所有 Python3 提交中击败了82.05%的用户
    内存消耗 : 17.5 MB, 在所有 Python3 提交中击败了5.31%的用户
"""

class NumArray:

    def __init__(self, nums):
        self.nums = nums
        sum_i = 0 # sum_i记录每个数字，从下标0加到当前数字的和
        target = [] 
        for i in range(len(nums)):
            sum_i += nums[i] # sum_i持续添加数字
            target.append(sum_i) # 把当前数字的sum_i加到结果中
        self.target = target

    def sumRange(self, i, j):
        return self.target[j]-self.target[i]+self.nums[i]        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    answer = obj.sumRange(2, 5)
    print(answer)