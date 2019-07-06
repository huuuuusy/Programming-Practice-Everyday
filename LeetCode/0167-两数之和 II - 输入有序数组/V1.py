""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    双指针
注意：
    返回的index要+1，和数组下标不同
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了86.82%的用户
    内存消耗 : 13.6 MB, 在所有 Python3 提交中击败了41.60%的用户
"""

class Solution:
    def twoSum(self, numbers, target):
        # 因为输入的数据一定有解，所以当长度为２时可以直接返回结果
        if len(numbers) == 2:
            return [1,2]
        # 双指针
        left = 0
        right = len(numbers) - 1
        # 判断左右指针指向元素的和
        # 根据和的情况移动指针
        for i in range(right):
            while left < right:
                if numbers[left] + numbers[right] < target:
                    left += 1
                elif numbers[left] + numbers[right] > target:
                    right -= 1
                else:
                    return [left+1, right+1]

if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    answer = Solution().twoSum(numbers, target)
    print(answer)