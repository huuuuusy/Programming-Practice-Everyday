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
结果：
    执行用时 : 32 ms, 在所有 Python3 提交中击败了99.37%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.10%的用户
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        # p和q均为空树时，二者相等
        if not p and not q:
            return True
        # p和q有且只有一个为空时，二者不相同
        if not p or not q:
            return False
        # 当p和q均为非空时，比较二者的值
        if p.val != q.val:
            return False
        # 递归比较二者的值
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)



if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    res = Solution().isSameTree(p, q)
    print(res)