""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    递归
结果：
    执行用时 : 340 ms, 在所有 Python3 提交中击败了36.03%的用户
    内存消耗 : 49.7 MB, 在所有 Python3 提交中击败了5.54%的用户
"""

class Solution:
    def reverseString(self, s):
        def helper(start,end,ls):
            # 判定递归的终止条件
            if start >= end:
                return 
            # 交换首尾元素
            ls[start], ls[end] = ls[end], ls[start]
            return helper(start+1, end-1, ls)
        helper(0, len(s)-1, s)
        return s

            


        
if __name__ == "__main__":
    nums = ["h","e","l","l","o"]
    answer = Solution().reverseString(nums)
    print(answer)
        