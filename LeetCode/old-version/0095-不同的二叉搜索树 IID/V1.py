""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    卡特兰数问题+递归解决
    我们从序列 1 ..n 中取出数字 i，作为当前树的树根。于是，剩余 i - 1 个元素可用于左子树，n - i 个元素用于右子树。
    这样会产生 G(i - 1) 种左子树 和 G(n - i) 种右子树，其中 G 是卡特兰数。
    现在，我们对序列 1 ... i - 1 重复上述过程，以构建所有的左子树；然后对 i + 1 ... n 重复，以构建所有的右子树。
    这样，我们就有了树根 i 和可能的左子树、右子树的列表。
    最后一步，对两个列表循环，将左子树和右子树连接在根上。
参考：
    https://baike.baidu.com/item/%E5%8D%A1%E7%89%B9%E5%85%B0%E6%95%B0
结果：
    执行用时 : 104 ms, 在所有 Python3 提交中击败了30.40%的用户
    内存消耗 : 15.5 MB, 在所有 Python3 提交中击败了5.32%的用户
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        def generate_trees(start, end):
            if start > end:
                return [None,]
            
            all_trees = []
            for i in range(start, end + 1):  # 选择根节点
                # 所有可能的左子树
                left_trees = generate_trees(start, i - 1)                
                # 所有可能的右子树
                right_trees = generate_trees(i + 1, end)                
                # 将左右子树和根节点相连
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            return all_trees
        return generate_trees(1, n) if n else []

if __name__ == "__main__":
    n = 3
    res = Solution().generateTrees(n)
    
    