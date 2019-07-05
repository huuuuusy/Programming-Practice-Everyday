""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    使用int()和bin()完成数据类型转换
注意:
    bin()使用后需要从第三个字符开始截断
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了88.43%的用户
    内存消耗 : 12.9 MB, 在所有 Python3 提交中击败了98.64%的用户
"""

class Solution:
    def addBinary(self, a, b):
        result = bin(int(a, 2) + int(b, 2))
        return result[2:]

if __name__ == "__main__":
    a = '11'
    b = '1'
    answer = Solution().addBinary(a, b)
    print(answer)