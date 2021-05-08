""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    用字典记录每个点和其他点的距离，如果某个距离出现第二次，则次数×2
    然后清空字典，记录下一个点
结果：
    执行用时 : 1124 ms, 在所有 Python3 提交中击败了93.10%的用户
    内存消耗 : 13.4 MB, 在所有 Python3 提交中击败了23.08%的用户
"""

class Solution:
    def numberOfBoomerangs(self, points):
        dist_dict = {}  # 相同距离出现的次数
        res = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    dist = (points[i][0]-points[j][0])*(points[i][0]-points[j][0]) + (points[i][1]-points[j][1])*(points[i][1]-points[j][1])
                    if dist not in dist_dict:
                        dist_dict[dist] = 1
                    else:
                        res += 2*dist_dict[dist]  # 如果数量增加1，结果增加2n
                        dist_dict[dist] += 1
            # 清空字典，记录下一个点
            dist_dict = {}
        return res

            

if __name__ == "__main__":
    points = [[0,0],[1,0],[2,0]]
    answer = Solution().numberOfBoomerangs(points)
    print(answer)
