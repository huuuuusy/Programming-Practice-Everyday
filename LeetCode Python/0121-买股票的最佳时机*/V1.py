""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    按时间顺序，从前到后遍历股票价格数组prices，每次迭代做两件事：
        统计直至目前的最低成本cost，因为今日卖出的利润等于今日price减去前几日的price最小值（即最小成本）
        计算直至目前的最高利润profit 
    最终，返回最高利润profit
注意：
    cost初始化值要足够大
结果：
    执行用时 : 60 ms, 在所有 Python3 提交中击败了77.51%的用户
    内存消耗 : 13.4 MB, 在所有 Python3 提交中击败了99.58%的用户
"""

class Solution:
    def maxProfit(self, prices):
        if prices == []:
            return 0
        cost = max(prices)
        profit = 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit


if __name__ == "__main__":
    s = [7,1,5,3,6,4]
    answer = Solution().maxProfit(s)
    print(answer)