""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路：
    使用filter + lambda对数组进行筛选
结果：
    本地运行可以，但是无法通过测试，猜测网站测试不允许对nums进行filter操作
    本思路可以作为日常使用的参考
"""

class Solution:
    def removeElement(self, nums, val):
        nums = filter(lambda num : num != val, nums)
        nums = [num for num in nums]
        return len(nums)



if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    answer = Solution().removeElement(nums, val)
    print(answer)