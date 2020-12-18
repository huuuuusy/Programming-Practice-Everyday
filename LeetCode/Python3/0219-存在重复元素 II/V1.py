""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    用滑动窗口优化后时空复杂度可以接受
结果：
    执行用时 : 76 ms, 在所有 Python3 提交中击败了35.01%的用户
    内存消耗 : 23.8 MB, 在所有 Python3 提交中击败了5.06%的用户
"""

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        # 用字典存储下标
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i],[]) + [i]
        for key,value in d.items():
            if len(value) == 1:
                continue
            else:
                # 检查下标之间的最小差值是否不超过k
                dist = []
                for i in range(len(value)-1):
                    dist.append(value[i+1]-value[i])
                if min(dist) <= k:
                    return True
        return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    k = 3
    answer = Solution().containsNearbyDuplicate(nums, k)
    print(answer)