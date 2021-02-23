""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    简单题
结果：
    执行用时 : 124 ms, 在所有 Python3 提交中击败了16.76%的用户
    内存消耗 : 15.2 MB, 在所有 Python3 提交中击败了5.42%的用户
"""

class Solution:
    def peakIndexInMountainArray(self, A):
        return A.index(max(A))

if __name__ == "__main__":
    A = [0,2,1,0]
    answer = Solution().peakIndexInMountainArray(A)
    print(answer)