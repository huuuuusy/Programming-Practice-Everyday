""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    需要理解题意
    如果是快乐数，则最终将进入全1的循环、
    如果不是快乐数，则会最后都会进入 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 的循环
    所以如果列表中出现已经检查过的数字的平方和且该数字不是1,说明进入非快乐数的循环
结果：
    执行用时 : 28 ms, 在所有 Python3 提交中击败了83.51%的用户
    内存消耗 : 11.7 MB, 在所有 Python3 提交中击败了29.07%的用户
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 当n为0时直接返回false
        if n == 0:
            return  False
        # 将目前检查过的数字的平方和放入列表中
        # 如果后面出现重复，则陷入循环，即非快乐数
        list_check = []
        while n != 1:
            strings = str(n)
            count = 0
            # 存入当前数字平方和
            for string in strings:
                count += int(string)**2
            # 判断平方和是否在列表中
            if count in list_check:
                return False
            else:
                list_check.append(count)
            n = count
        return True       

if __name__ == "__main__":
    n = 19
    answer = Solution().isHappy(n)
    print(answer)