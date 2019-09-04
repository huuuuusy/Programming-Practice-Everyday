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
    执行用时 : 44 ms, 在所有 Python3 提交中击败了85.23%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def defangIPaddr(self, address):
        res =""
        for num in address:
            if  num == '.':
                res += '[.]'
            else:
                res += num
        return res
                

if __name__ == "__main__":
    address = "1.1.1.1"
    answer = Solution().defangIPaddr(address)
    print(answer)