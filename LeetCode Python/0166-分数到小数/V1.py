""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.40
工具： python == 3.7.3
"""

"""
思路:
    注意对小数进行分情况讨论
结果：
    执行用时 : 40 ms, 在所有 Python3 提交中击败了87.27%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了6.17%的用户
"""

class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0: return "0" # 分子为0则返回0
        res = []
        # 首先判断结果正负, 异或作用就是 两个数不同 为 True 即 1 ^ 0 = 1 或者 0 ^ 1 = 1
        if (numerator > 0) ^ (denominator > 0): # 如果分子或者分母不同号，则结果添加负号
            res.append("-")    
        numerator, denominator = abs(numerator), abs(denominator)
        # 判读到底有没有小数
        a, b = divmod(numerator, denominator) # 求出商和余数
        res.append(str(a)) # 将商加入结果

        # I. 如果余数为0，表示整除，结果无小数
        if b == 0:
            return "".join(res) # 直接输出商

        # II. 如果余数不为0，表示需要添加小数部分
        res.append(".")
        # 处理余数
        # 把所有出现过的余数记录下来
        loc = {b: len(res)}
        while b:
            b *= 10
            a, b = divmod(b, denominator)
            res.append(str(a))
            # 余数前面出现过,说明开始循环了,加括号
            if b in loc:
                res.insert(loc[b], "(")
                res.append(")")
                break
            # 在把该位置的记录下来
            loc[b] = len(res)
        return "".join(res)

if __name__ == "__main__":
    numerator = 2
    denominator = 3
    answer = Solution().fractionToDecimal(numerator, denominator)
    print(answer)