""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
"""

"""
思路：
    双循环确定前两个数字
    内嵌双指针确定后两个数字
    注意可以通过当前组合的最小值和最大值判断是否跳出循环从而节省时间
    需要清晰的思路去判断每种情况
结果：
    执行用时 : 108 ms, 在所有 Python3 提交中击败了96.93%的用户
    内存消耗 : 12.9 MB, 在所有 Python3 提交中击败了98.35%的用户
"""

class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        # 先排除不够4个数的情况
        if n < 4:
            return []
        # 将数字按从小到大排序
        nums.sort()
        res = []
        # 最外圈循环，从最左边移动到倒数第三个数
        for i in range(n-3):
            # 防止重复的数字进入res（因为若连续的数字相等，他们遍历右边后得到的结果也相同）
            if i>0 and nums[i]==nums[i-1]:
                continue
            # 当数组最小值已经大于target，则跳出
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target:
                break
            # 当数组最大值仍然小于target,说明起点的i太小，换下一个
            if nums[i]+nums[n-1]+nums[n-2]+nums[n-3] < target:
                continue
            # 第二层循环，从i右边起移动到倒数第二个数字
            for j in range(i+1, n-2):
                # 防止重复数字进入res
                if j-i>1 and nums[j]==nums[j-1]:
                    continue
                # 同理，当数组最小值大于target,跳出循环
                if nums[i]+nums[j]+nums[j+1]+nums[j+2] > target:
                    break
                # 同理，当数组最大值仍小于target,说明起点j太小，换下一个
                if nums[i]+nums[j]+nums[n-1]+nums[n-2] < target:
                    continue
                # 双指针找第三个和第四个数字
                left = j+1
                right = n-1
                while left < right:
                    tmp = nums[i]+nums[j]+nums[left]+nums[right]
                    if tmp == target:
                        res.append(([nums[i],nums[j],nums[left],nums[right]]))
                        while left<right and nums[left]==nums[left+1]:
                            left += 1
                        while left<right and nums[right]==nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif tmp > target:
                        right -= 1
                    else:
                        left += 1
        return res



if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    answer = Solution().fourSum(nums, target)
    print(answer)

