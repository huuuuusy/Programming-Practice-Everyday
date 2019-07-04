""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
"""

"""
思路:
    list --> str -->int
    int+1 --> str --> list
注意:
    中间要用str过渡，直接从数字转列表会出错
结果：
    执行用时 : 52 ms, 在所有 Python 提交中击败了79.45%的用户
    内存消耗 : 13.1 MB, 在所有 Python 提交中击败了83.63%的用户
"""

class Solution:
    def plusOne(self, digits):
        # 先将列表转为数字
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        original_num = "".join(digits)
        # 对数字+1后再转为列表
        plus_one = list(str(int(original_num) + 1))
        result = [int(x) for x in plus_one]
        return result

if __name__ == "__main__":
    nums =  [4,3,2,1]
    answer = Solution().plusOne(nums)
    print(answer)