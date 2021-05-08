""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    简单遍历
结果：
    执行用时 : 96 ms, 在所有 Python3 提交中击败了39.38%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.05%的用户
"""

class Solution:
    def selfDividingNumbers(self, left, right):
        res = []
        for i in range(left, right+1):
            nums = list(str(i))
            flag = True
            for num in nums:
                # 如果某一位有0或者某一位无法被整除，直接跳出内层循环
                if int(num) == 0 or i%int(num) != 0:
                    flag = False
                    break
            if flag == True:
                res.append(i)
        return res
                
        
 
if __name__ == "__main__":
    left = 1
    right = 22
    answer = Solution().selfDividingNumbers(left, right)
    print(answer)