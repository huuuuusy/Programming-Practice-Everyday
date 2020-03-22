""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    BFS
链接：
    https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/pythonfei-di-gui-de-bfshe-dfs-by-baiyizhe/
结果：
    执行用时 : 68 ms, 在所有 Python3 提交中击败了58.50%的用户
    内存消耗 : 15 MB, 在所有 Python3 提交中击败了86.14%的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = []
        queue.append((1,root))
        depth = 0
        while queue:
            cur_dep, node = queue.pop(0)
            depth = max(depth, cur_dep)
            if node.left is not None:
                queue.append((cur_dep+1,node.left))
            if node.right is not None:
                queue.append((cur_dep+1,node.right))
        return depth
