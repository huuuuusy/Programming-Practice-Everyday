#两数之和-暴力解法

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """       
        l = len(nums)
        for i in range(l-1):
            for j in range(i+1,l):
                if nums[i] + nums[j] == target:
                    return [i,j]

#两数之和-哈希解法
class Solution:
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i
            else:
                return map[nums[i]], i

#两数之和-双指针解法
class Solution:
    def twoSum(self, nums, target):
        array = nums.copy()
        nums.sort()
        i, j = 0, len(nums)-1
        while i<j:
            s = nums[i] + nums[j]
            if s<target:
                i += 1
            elif s>target:
                j -= 1
            else:
                break
 
        res = []
        for k in range(len(nums)):
            if array[k] == nums[i] or array[k] == nums[j]:
                res.append(k)
        return res
#两数之和-魔改
class Solution:
 def twoSum(self, nums, target):
        #先对数组排序
          nums.sort() #左右指针
          lo, hi = 0, len(nums)-1
          while lo<hi:
            s = nums[lo] + nums[hi]
            if s<target:
                lo += 1
            elif s>target:
                hi -= 1
            elif s == target:
                return [nums[lo],nums[hi]]
#两数之和-再魔改
class Solution:
    def twoSumTarget(self, nums, target):      #先对数组排序          nums.sort()
          res = []      #左右指针          lo, hi = 0, len(nums)-1
          left = nums[lo]
          right = nums[hi]
          while lo<hi:
            s = nums[lo] + nums[hi]
            if s<target:
                lo += 1
            elif s>target:
                hi -= 1
            elif s == target:
                res.append([nums[lo],nums[hi]])
                while lo < hi and nums[lo] == left:
                     lo += 1
                while lo < hi and nums[hi] == right:
                     hi -= 1
          return res
#167两数之和
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low < high:
            total = numbers[low] + numbers[high]
            if total == target:
                return [low + 1, high + 1]
            elif total < target:
                low += 1
            else:
                high -= 1

        return [-1, -1]
#三数之和
class Solution:
    def threeSum(self,nums):
        # 排序
        nums.sort()

        # 单循环+双指针
        res = []

        for i in range(len(nums)):
            # 去重（如果当前C位数和相邻的数相等，直接移动指针）
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i],nums[left],nums[right]])

                    # 去重（如果当前数和相邻的数相等，直接移动指针）
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

        return res
#最接近的三数之和
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 排序
        nums.sort()

        # 初始化
        a = abs(nums[0] + nums[1] + nums[2] - target)
        res = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            # 当前nums[i]情况下，搜索最接近的组合
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                # 比较sums与目标target的距离与之前最近的距离，如果更近则更新
                if abs(sums-target) < a:
                    a = abs(sums-target)
                    res = sums
                
                if sums > target:
                    right -= 1
                elif sums < target:
                    left += 1
                # 如果sums == target，则说明距离为0，这就是最接近的数
                elif sums == target:
                    return sums
        return res
#四数之和
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = list()
        if not nums or len(nums) < 4:
            return res
        
        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return res
#盛最多水
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, res = 0, len(height) - 1, 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res
#有效三角形个数
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 排序
        nums.sort()

        count = 0
        for i in range(2,len(nums)):
            
            left = 0
            right = i - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    # 这些都可以：[left,right]、[left+1,right]...[right-1,right]
                    count += right - left
                    right -= 1
                else:
                    left += 1
        
        return count
#leetcode26
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i+1
#leetcode 27
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        last = len(nums)-1
        while j <= last:
            if nums[j] == val:
                nums[j] = nums[last]
                last -= 1
            else:
                j += 1
        return last+1
#leetcode80
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        i = 0
        j = 1
        while j < len(nums):
            # 二者元素相同（重复元素）
            if nums[i] == nums[j]:
                count += 1
                # 这个元素正好重复了2次
                if count == 2:
                    i += 1
                    nums[i] = nums[j]
                # 这个元素重复多于2次
                else:
                    pass
                j += 1
            # 二者元素不同（新元素）
            else:
                i += 1
                nums[i] = nums[j]
                count = 1
                j += 1
        return i+1
#leetcode283
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0
        # 双指针遍历寻找非零元素
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        
        # 空位置赋0
        for k in range(i,len(nums)):
            nums[k] = 0
#leetcode845
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        
        res = 0

        # 固定山峰
        for i in range(1,len(A)-1):
            # 只有当前点为山峰的情况，才在左右寻找最长山峰
            if A[i-1] < A[i] and A[i+1] < A[i]:
                left = i - 1
                right = i + 1

                # 左半边山脉的长度
                while left >= 0 and A[left] < A[left+1]:
                    left -= 1

                # 右半边山脉的长度
                while right <= len(A)-1 and A[right] < A[right-1]:
                    right += 1

                # 如果这个山脉比最长的山脉长，更新res
                if right - left - 1 > res:
                    res =  right - left - 1
        
        return res
#leetcode239
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ##双指针的方式
        res = []
        L = 0
        R = L+k
        if len(nums)>0:
            while R<len(nums)+1:
                maxValue = max(nums[L:R])
                res.append(maxValue)
                L+=1
                R+=1
            return res
        else:
            return nums
#leetcode209
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 初始化
        left,sums,res = 0,0,float('inf')

        # 右指针右移
        for right in range(len(nums)):
            sums += nums[right]
            while sums >= s:
                # 若新值小于旧值，更新res
                if right - left + 1 < res:
                    res = right - left + 1
                # 左指针向右滑动
                sums -= nums[left]
                left += 1

        return 0 if res == float('inf') else res
#leetcode713
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:        
        left = 0
        product = 1
        count = 0
        for right in range(len(nums)):
            # 右边界右移
            product *= nums[right]
            # 如果乘积>=k，左边界右移
            while left <= right and product >= k:
                product /= nums[left]
                left += 1
            # 当前右边界下，满足条件的数组
            count += right - left + 1
        return count
#leetcode350
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 排序
        nums1.sort()
        nums2.sort()

        i,j = 0,0
        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
        
        return res
#leetcode349
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 排序
        nums1.sort()
        nums2.sort()

        i,j = 0,0
        nums_set = set()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] == nums2[j]:
                nums_set.add(nums1[i])
                i += 1
                j += 1
        
        return nums_set
