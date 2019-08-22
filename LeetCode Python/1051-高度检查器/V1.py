""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    python无脑法
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了63.42%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def heightChecker(self, heights):
        right_heights = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != right_heights[i]:
                res += 1 
        return res

if __name__ == "__main__":
    heights = [1,1,4,2,1,3]
    answer = Solution().heightChecker(heights)
    print(answer)