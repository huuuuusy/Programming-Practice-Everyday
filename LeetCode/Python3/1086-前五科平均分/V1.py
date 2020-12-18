""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    字典保存每一条记录，然后取出前5进行计算
结果：
    执行用时 : 116 ms, 在所有 Python3 提交中击败了15.84%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def highFive(self, items):
        d = {}
        # 保存每一条记录
        for item in items:
            d[item[0]] = d.get(item[0],[]) + [item[1]]
        result = []
        # 取出记录进行计算
        for key in sorted(d.keys()):
            ID_result = [key]+[int(sum(sorted(d[key])[::-1][:5])/5)]
            result.append(ID_result)
        return result
        
if __name__ == "__main__":
    items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    answer = Solution().highFive(items)
    print(answer)