""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    利用字典的get()函数
    key是num,value是次数
    如果字典中已经有num，则返回num的value，否则返回0；并且+1
    最后在字典中查找出现一次的元素(value=1)，并返回key
结果：
    执行用时 : 64 ms, 在所有 Python3 提交中击败了50.86%的用户
    内存消耗 : 15.1 MB, 在所有 Python3 提交中击败了7.47%的用户
"""

class Solution:
    def singleNumber(self, nums):
        nums_dict = {}
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1

        for key, val in nums_dict.items():
            if val == 1:
                return key

if __name__ == "__main__":
    nums = [4,1,2,1,2]
    answer = Solution().singleNumber(nums)
    print(answer)

    