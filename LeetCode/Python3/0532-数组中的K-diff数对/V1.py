""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    用两个集合分别存储已经检查的数字和当前k-diff中的较小数字
    只需要一轮循环
    如果使用双重循环的暴力解法，某些测试用例会超时
结果：
    执行用时 : 180 ms, 在所有 Python3 提交中击败了75%的用户
    内存消耗 : 15.5 MB, 在所有 Python3 提交中击败了7.40%的用户
"""

class Solution:
    def findPairs(self, nums, k):
        if k < 0: return 0 
        saw, diff = set(), set() # saw用来存储检查过的数字，diff存储k-diff中较小的数字
        for num in nums:
            if num-k in saw: # 如果已经检查过较小的数字
                diff.add(num-k)
            if num+k in saw: # 如果当前数字是较小的数字
                diff.add(num)
            saw.add(num) # 将当前数字存到已经检查的集合中　
        return len(diff)

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    k = -1
    answer = Solution().findPairs(nums, k)
    print(answer)


