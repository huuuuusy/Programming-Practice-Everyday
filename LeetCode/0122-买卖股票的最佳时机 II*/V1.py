""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    一定要分析题意：
    考虑买股票的策略：设今天价格p1，明天价格p2，若p1 < p2则今天买入明天卖出，赚取p2 - p1
    若遇到连续上涨的交易日，第一天买最后一天卖收益最大，等价于每天买卖（因为没有交易手续费）
        遇到价格下降的交易日，不买卖，因此永远不会亏钱
        赚到了所有交易日的钱，所有亏钱的交易日都未交易，理所当然会利益最大化
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了94.93%的用户
    内存消耗 : 13.4 MB, 在所有 Python3 提交中击败了99.20%的用户
"""

class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp > 0:
                profit += tmp
        return profit

if __name__ == "__main__":
    s = [7,1,5,3,6,4]
    answer = Solution().maxProfit(s)
    print(answer)