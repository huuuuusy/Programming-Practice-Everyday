""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    哈希表直接列出所有情况计算
结果：
    执行用时 : 72 ms, 在所有 Python3 提交中击败了82.43%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.26%的用户
"""

class Solution:
    def intToRoman(self, num):
        lookup = {
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            400:'CD',
            500:'D',
            900:'CM',
            1000:'M'     
        }
        res = ""
        for key in sorted(lookup.keys())[::-1]:
            a = num // key
            if a == 0:
                continue
            res += (lookup[key] * a)
            num -= a * key
            if num == 0:
                break
        return res

if __name__ == "__main__":
    s = 8
    answer = Solution().intToRoman(s)
    print(answer)