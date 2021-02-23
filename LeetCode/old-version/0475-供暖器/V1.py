""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    二分法
结果：
    执行用时 : 584 ms, 在所有 Python3 提交中击败了24.52%的用户
    内存消耗 : 17.2 MB, 在所有 Python3 提交中击败了8.96%的用户
"""

class Solution:
    def findRadius(self, houses, heaters):
        # 存放每个房屋与加热器的最短距离
        res = 0
        # 排序
        houses.sort()
        heaters.sort()
        # 遍历所有的房子
        for house in houses:
            # 二分法查找供暖器
            left = 0
            right = len(heaters) - 1 
            while left < right:
                mid = (left + right + 1) >> 1
                if heaters[mid] > house:
                    right = mid - 1 # 右边界收缩
                else:
                    left = mid
            #print(house,heaters[left])
            # 如果供暖器和房子相同，则跳过
            if heaters[left] == house:
                continue
            # 否则比较房子和左右两端供暖器距离，找到最近的供暖器
            else:
                if left+1 <= len(heaters)-1:
                    res = max(res, min(abs(heaters[left]-house), abs(heaters[left+1]-house)))
                else:
                    res = max(res, abs(heaters[left]-house))
        return res
    

if __name__ == "__main__":
    houses, heaters = [1,5],[2]
    answer = Solution().findRadius(houses, heaters)
    print(answer)