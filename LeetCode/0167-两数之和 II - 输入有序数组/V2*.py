""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    字典
    先把当前元素的目标差值元素存入字典
    然后当新元素出现时，比较字典中是否已经存入该元素
    如果存在，说明新元素是之前某元素的目标差值
    此时返回之前元素和当前新元素
注意：
    字典的键是目标差值元素，值是当前元素的index+1
    这样当目标差值元素出现时，可以直接找到之前元素的索引
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了86.82%的用户
    内存消耗 : 13.４MB, 在所有 Python3 提交中击败了95.93%的用户
"""

class Solution:
    def twoSum(self, numbers, target):
        dictionary = {}
        for i in range(len(numbers)):
            obj = target - numbers[i]
            if numbers[i] in dictionary:
                return [dictionary[numbers[i]], i+1]
            else:
                dictionary[obj] = i + 1
        

if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    answer = Solution().twoSum(numbers, target)
    print(answer)