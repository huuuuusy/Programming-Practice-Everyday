""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    先将第一个数组排序，然后用left作为指针找到序列中0元素的位置
    之后对0元素依次替换即可
注意：
    不允许新建其他数组，只能在nums1的空间中进行操作，所以复制的方法需要放弃
结果：
    执行用时 : 32 ms, 在所有 Python3 提交中击败了99.90%的用户
    内存消耗 : 13.1 MB, 在所有 Python3 提交中击败了63.93%的用户
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.sort()
        left = 0
        # 寻找0元素的起始位置
        for i in range(m):
            if nums1[left] != 0:
                left += 1
        # 替换0元素
        k = 0
        for j in range(left, left + n):
            nums1[j] = nums2[k]
            k += 1
        nums1.sort() 
        return nums1


if __name__ == "__main__":
    nums1 =  [-10,-10,-10,-10,-10,-10,-9,-9,-9,-8,-8,-8,-8,-7,-7,-7,-7,-6,-6,-6,-6,-5,-5,-5,-4,-4,-3,-3,-3,-3,-3,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,-1,0,1,1,1,1,1,2,3,3,3,3,3,3,4,4,5,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    m = 75
    nums2 = [-10,-10,-10,-8,-8,-6,-6,-6,-6,-4,-4,-4,-3,-3,-3,-3,-2,-1,1,1,1,1,2,3,4,5,5,6,6,6,8,8,8,9,9]
    n = 35
    answer = Solution().merge( nums1, m, nums2, n)
    print(answer)
    