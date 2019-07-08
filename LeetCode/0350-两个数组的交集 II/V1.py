""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    将两个数组排序
    然后从第一个数组依次读取数字，判断第二个数组是否存在对应数字
    如果存在则保存结果，并将该数字从第二个数组推出
结果：
    执行用时 : 68 ms, 在所有 Python3 提交中击败了64.95%的用户
    内存消耗 : 12.8 MB, 在所有 Python3 提交中击败了99.33%的用户
"""

class Solution:
    def intersect(self, nums1, nums2):
        result = []
        index = 0
        nums1.sort()
        nums2.sort()
        for num in nums1:
            if num in nums2:
                index = nums2.index(num)
                result.append(num)
                nums2.pop(index)
        return result


if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2]
    answer = Solution().intersect(nums1, nums2)
    print(answer)

