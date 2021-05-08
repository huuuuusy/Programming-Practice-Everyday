""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.39
工具： python == 3.7.3
"""

"""
思路:
    递归
参考:
    https://leetcode-cn.com/problems/symmetric-tree/solution/pythondi-gui-he-dui-lie-shi-xian-dui-cheng-er-ch-2/
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了69.37%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了5.03%的用户
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root: return True # 空树是对称二叉树
        return self.isMirror(root.left, root.right) # 将原始的树分成左右两个子树进行判断

    def isMirror(self, p, q): # 判断两个树是否为镜像树
        if not p and not q: # 两个空树是镜像树
            return True
        if not p or not q: # 一个空树和一个非空树不是镜像树
            return False
        l = self.isMirror(p.left, q.right) # 比较p的左子树和q的右子树是否为镜像树
        r = self.isMirror(p.right, q.left) # 比较p的右子树和q的左子树是否为镜像树
        return p.val == q.val and l and r # 当且仅当根节点相同、l和r均返回True时，才可以整体返回True
        

if __name__ == "__main__":
    t = TreeNode(1)
    t.left = t1 = TreeNode(2)
    t1.left = TreeNode(3)
    t1.right = TreeNode(4)
    t.right = t2 = TreeNode(2)
    t2.left = TreeNode(4)
    t2.right = TreeNode(3)
    root = t
    res = Solution().isSymmetric(root)
    print(res)