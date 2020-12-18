""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.39
工具： python == 3.7.3
"""

"""
思路：
    移位
参考：
    https://leetcode-cn.com/problems/divide-two-integers/solution/xiao-xue-sheng-du-hui-de-lie-shu-shi-suan-chu-fa-b/
结果：
    执行用时 : 68 ms, 在所有 Python3 提交中击败了35.12%的用户
    内存消耗 : 13.2 MB, 在所有 Python3 提交中击败了８0.78%的用户
"""

class Solution:
    def divide(self, dividend, divisor):
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend) 
        divisor = abs(divisor)
        count = 0
        #把除数不断左移，直到它大于被除数
        while dividend >= divisor:
            count += 1
            divisor <<= 1 # 左移一位表示乘以2
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1 # 右移一位表示除以2
            if divisor <= dividend:
                result += 1 << count #这里的移位运算是把二进制（第count+1位上的1）转换为十进制
                dividend -= divisor
        if sign: result = -result
        return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1 



if __name__ == "__main__":
    dividend = 10
    divisor = 3
    answer = Solution().divide(dividend, divisor)
    print(answer)