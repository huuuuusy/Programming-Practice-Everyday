""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    二分查找
结果：
    执行用时 : 184 ms, 在所有 Python3 提交中击败了6.03%的用户
    内存消耗 : 14.9 MB, 在所有 Python3 提交中击败了5.42%的用户
"""

class Solution:
    def peakIndexInMountainArray(self, A):
        left = 0 
        right = len(A) - 1 
        while left < right:
            # 因为后面是右边界收缩，所以用右中位数
            mid = (left + right + 1) >> 1 
            # 如果满足如下条件，则是峰顶
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid 
            # 开始进入二分的判断
            # if分支是要舍去的部分，此处需要舍去已经进入下降环节的列表值
            # 所以是右边界收缩
            if A[mid] < A[mid-1] and A[mid] > A[mid+1]:
                right = mid - 1
            # else分支是需要接着找mid的部分，直接写左边界
            else:
                left = mid
        return -1 


if __name__ == "__main__":
    A = [0,2,1,0]
    answer = Solution().peakIndexInMountainArray(A)
    print(answer)