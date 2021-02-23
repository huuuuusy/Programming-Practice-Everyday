""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    动态规划
结果：
    执行用时 : 88 ms, 在所有 Python3 提交中击败了64.29%的用户
    内存消耗 : 14.1 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def minCost(self, costs):
        # 排除特殊情况
        if len(costs) == 0:
            return 0
        # res存储所有粉刷方案的结果
        res = []
        # 对于第一个房子，不用考虑和其他房子的关系，可以直接存入
        a = costs[0]
        res.append(a)
        # 对于从第二个房子开始的所有房子：
        for i in range(1, len(costs)):
            a = [0]*3 
            # a负责存储当前房子和上一个房子的所有颜色方案
            # 对于每种颜色，都和上一个房子中不属于这个颜色的粉刷方案组合，取最小值存入
            a[0] = min((costs[i][0]+res[-1][1]),(costs[i][0]+res[-1][2]))
            a[1] = min((costs[i][1]+res[-1][0]),(costs[i][1]+res[-1][2]))
            a[2] = min((costs[i][2]+res[-1][0]),(costs[i][2]+res[-1][1]))
            print(a)
            res.append(a)
        # 最后的返回值是最后一个房子的最小值方案
        return min(res[-1])




        
if __name__ == "__main__":
    costs = [[17,2,17],[16,16,5],[14,3,19]]
    answer = Solution().minCost(costs)
    print(answer)


