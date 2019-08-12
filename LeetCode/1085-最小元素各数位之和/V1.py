""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    无难度
结果：
    执行用时 : ４２ ms, 在所有 Python3 提交中击败了92.73%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def sumOfDigits(self, A):
        min_num = list(str(min(A)))
        # 用map函数将字符转化为整数
        return 1 if sum(map(int,min_num)) %2 == 0 else 0

if __name__ == "__main__":
    A = [99,77,33,66,55]
    answer = Solution().sumOfDigits(A)
    print(answer)