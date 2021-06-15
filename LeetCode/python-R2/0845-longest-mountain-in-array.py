"""
我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：

B.length >= 3
存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给出一个整数数组 A，返回最长 “山脉” 的长度。

如果不含有 “山脉” 则返回 0。


示例 1：
输入：[2,1,4,7,3,2,5]
输出：5
解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。

示例 2：
输入：[2,2,2]
输出：0
解释：不含 “山脉”。
 
提示：
0 <= A.length <= 10000
0 <= A[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-mountain-in-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 双指针
# 固定山峰，然后左右使用双指针去寻找

class Solution:
    def longestMountain(self, arr):
        res = 0
        
        # 固定山峰
        for i in range(1,len(arr)-1):
            # 只有当前点为山峰的情况，才在左右寻找最长山峰
            if arr[i-1] < arr[i] and arr[i+1] < arr[i]:
                left = i - 1
                right = i + 1

                # 左半边山脉的长度
                while left >= 0 and arr[left] < arr[left+1]:
                    left -= 1

                # 右半边山脉的长度
                while right <= len(arr)-1 and arr[right] < arr[right-1]:
                    right += 1

                # 如果这个山脉比最长的山脉长，更新res
                if right - left - 1 > res:
                    res =  right - left - 1
        
        return res        
                
                
if __name__ == '__main__':
    arr = [0,1,0]
    answer = Solution().longestMountain(arr)
    print(answer)