""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    双指针直接交换元素
结果：
    执行用时 : 208 ms, 在所有 Python3 提交中击败了66.03%的用户
    内存消耗 : 17.4 MB, 在所有 Python3 提交中击败了93.54%的用户
"""

class Solution:
    def reverseString(self, s):
        left = 0
        right = len(s)-1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


        
if __name__ == "__main__":
    nums = ["h","e","l","l","o"]
    answer = Solution().reverseString(nums)
    print(answer)
        