""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.39
工具： python == 3.7.3
"""

"""
思路:
    确定上下界，在搜索左右子树时，确定左右子树的根节点和上下界的关系
    递归求解
结果：
    执行用时 : 60 ms, 在所有 Python3 提交中击败了85.37%的用户
    内存消耗 : 16.3 MB, 在所有 Python3 提交中击败了25.68%的用户
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root, low = float('-inf'), high = float('inf')): # 修改函数定义
        if not root: return True # 空树是二叉搜索树
        if not low < root.val < high: return False # 如果节点的值不满足上下界的要求，则返回False
        return self.isValidBST(root.left, low, root.val) and self.isValidBST(root.right, root.val, high)


if __name__ == "__main__":
    t1 = TreeNode(5)
    t1.left = TreeNode(1)
    t1.right = t2 = TreeNode(4)
    t2.left = TreeNode(3)
    t2.right = TreeNode(6)
    root = t1
    res = Solution().isValidBST(root)
    print(res)