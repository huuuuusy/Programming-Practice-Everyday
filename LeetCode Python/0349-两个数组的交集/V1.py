""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    先用set将两个数组分别去重
    然后合并后的列表中如果某元素数目大于1,说明其来自不同的数组
    利用字典保存结果并且判断
结果：
    执行用时 : 44 ms, 在所有 Python3 提交中击败了97.64%的用户
    内存消耗 : 13.1 MB, 在所有 Python3 提交中击败了81.55%的用户
"""

class Solution:
    def intersection(self, nums1, nums2):
        d = {}
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        for num in nums1 + nums2:
            d[num] = d.get(num, 0) + 1
        result = []
        for key, value in d.items():
            if value > 1:
                result.append(key)
        return result

if __name__ == "__main__":
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    answer = Solution().intersection(nums1, nums2)
    print(answer)