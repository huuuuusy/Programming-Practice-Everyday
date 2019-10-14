""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.39
工具： python == 3.7.3
"""

"""
思路:
    字典直接求解
结果：
    执行用时 : 40 ms, 在所有 Python3 提交中击败了88.89%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def isStrobogrammatic(self, num):
        lookup = {
            "6" : "9",
            "9" :"6",
            "8" : "8",
            "1" : "1",
            "0" :"0"
        }
        rotate_num = ""
        for a in num:
            if a in lookup:
                rotate_num += lookup[a]
            else:
                return False
        return rotate_num[::-1] == num
 

if __name__ == "__main__":
    num = "101"
    answer = Solution().isStrobogrammatic(num)
    print(answer)