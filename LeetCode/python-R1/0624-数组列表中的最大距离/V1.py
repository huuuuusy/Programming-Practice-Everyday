""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    双重循环，第120个测试用例超时
"""

class Solution:
    def maxDistance(self, arrays):
        min_array = [min(array) for array in arrays]
        max_array = [max(array) for array in arrays]
        ans = 0
        for i in range(len(min_array)):
            for j in range(len(max_array)):
                if i != j:
                    ans = max(abs(min_array[i]-max_array[j]),ans)
        return ans

if __name__ == "__main__":
    arrays = [[1,2,3],[4,5],[1,2,3]]
    answer = Solution().maxDistance(arrays)
    print(answer)