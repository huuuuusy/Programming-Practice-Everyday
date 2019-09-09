""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    卡特兰数问题
    假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数，则
        G(n)=f(1)+f(2)+f(3)+f(4)+...+f(n)
    当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，则
        f(i)=G(i−1)∗G(n−i)
    综合两个公式可以得到 卡特兰数 公式
        G(n)=G(0)∗G(n−1)+G(1)∗(n−2)+...+G(n−1)∗G(0)
参考：
    https://baike.baidu.com/item/%E5%8D%A1%E7%89%B9%E5%85%B0%E6%95%B0
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了69.50%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了6.32%的用户
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def numTrees(self, n):
        dp = [1,1]
        for i in range(2,n+1):
            value = 0
            for j in range(1,i+1):
                value += dp[j-1] * dp[i-j]
                j += 1 
            dp.append(value)
            i += 1 
        return dp[n]

if __name__ == "__main__":
    n = 3
    res = Solution().numTrees(n)
    print(res)