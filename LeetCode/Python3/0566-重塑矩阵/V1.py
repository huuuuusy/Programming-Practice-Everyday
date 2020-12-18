""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    先排序，再两两一组进行计算
结果：
    执行用时 : 120 ms, 在所有 Python3 提交中击败了80.87%的用户
    内存消耗 : 14.9 MB, 在所有 Python3 提交中击败了5.47%的用户
"""

class Solution:
    def matrixReshape(self, nums, r, c):
        # 排除异常情况
        if len(nums)*len(nums[0]) !=r*c:
            return nums
        # 构建输出格式的全零矩阵
        ans = [[0]*c for _ in range(r)]
        # 初始化i,j
        i, j = 0, 0
        # 遍历ans的i,j
        for m in nums:
            for n in m:
                ans[i][j] = n
                j += 1
                # 当j遍历到这一列最后的时候，j跳回第一列，行数加一
                if j == c:
                    j = 0
                    i += 1 
        return ans


if __name__ == "__main__":
    nums = [[1,2],[3,4]]
    r = 1
    c = 4
    answer = Solution().matrixReshape(nums, r, c)
    print(answer)