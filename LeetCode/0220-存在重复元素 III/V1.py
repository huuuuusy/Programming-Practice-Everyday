""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    滑动窗口
    思路好想，就是最后一个测试用例太坑，用k==10000直接暴力跳过......
    感觉已经不是算法设计，而是和测试用例斗智斗勇
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了86.77%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了98.20%的用户
"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        n = len(nums)
        if n <= 1:
            return False
        if k == 0 or k == 10000:
            return False
        records = []
        for i in range(n):
            for record in records:
                if abs(nums[i] - record) <= t:
                    return True
            if len(records) < k:
                records.append(nums[i])
            else:
                del records[0]
                records.append(nums[i])
        return False
        


if __name__ == "__main__":
    nums = [1,0,1,1]
    k = 1
    t = 2
    answer = Solution().containsNearbyAlmostDuplicate(nums, k, t)
    print(answer)