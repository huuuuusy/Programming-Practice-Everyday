""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    双循环＋字典
结果：
    执行用时 : 164 ms, 在所有 Python3 提交中击败了40.95%的用户
    内存消耗 : 14.2 MB, 在所有 Python3 提交中击败了9.89%的用户
"""
from collections import Counter
class Solution:
    def maxPoints(self, points):
        # 排除特殊情况
        if len(points) < 3:
            return len(points)
        d = {} 
        res = []
        new_points = []
        # 将数组转化为元组
        for point in points:
            new_points.append(tuple(point))
        # 统计每个元素重复出现几次
        c = Counter(new_points)
        points = list(set(new_points))
        if len(points) == 1:
            return c[points[0]]
        # 在经过set()处理后的没有重复数字的list中循环
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                # 不在同一水平线上，避免分母为0
                if points[i][0]-points[j][0] != 0:
                    # 乘以一个大数，避免丢失精度（后面有一个测试用例会出现精度丢失）
                    k = ((points[i][1]-points[j][1]) / (points[i][0]-points[j][0])) * 10000000
                    b = points[i][1] - (k/10000000) * points[i][0]
                else:
                    # 在同一水平线上，直接写一个其他情况不可能出现的k,b值记录
                    k = 1000000000000 + points[i][0]
                    b = 0
                # 判断是否已存在这条直线
                if (k,b) not in d:
                    d[(k,b)] = []
                    for num in range(c[points[i]]):
                        d[(k,b)].append(points[i])
                    for num in range(c[points[j]]):
                        d[(k,b)].append(points[j])
                else:
                    if points[j] not in d[(k,b)]:
                        for num in range(c[points[j]]):
                            d[(k,b)].append(points[j])
        # 计数
        for k,v in d.items():
            d[k] = len(v)
        return max(d.values())


            

if __name__ == "__main__":
    points = [[0,0],[94911151,94911150],[94911152,94911151]]
    answer = Solution().maxPoints(points)
    print(answer)
