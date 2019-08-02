""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    对于二叉树中的任何一个节点而言，它都有两个角色需要扮演：
        一个是作为值存储的角色（角色1）
        另一个角色是作为它所带领的子树的一个代表（角色2）
    设置的bool变量，就是为了说明当前拿到的这个节点，应该是以一个值存储的这种角色对待它(True)，还是应该以一个子树的代表这种角色对待它（False）
    如果是前者，那么就简单的将其所存储的值打印出来，如果是后者，我们需要继续探索由它带领的子树。
链接：
    https://leetcode-cn.com/problems/two-sum/solution/xian-xu-zhong-xu-hou-xu-de-fei-di-gui-ban-ben-by-l/
结果：
    执行用时 : 44 ms, 在所有 Python3 提交中击败了88.50%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了5.32%的用户
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # st目前存储root节点，false表示root节点是子树的代表
        st=[(root,False)]
        res=[]
        while st:
            # cur是弹出的节点
            # vis是节点的flag
            cur,vis=st.pop()
            # 如果flag是True,表示节点仅代表其存储的值，将这个值添加到结果中
            if vis:
                res.append(cur.val)
            # 如果flag是False,表示节点代表整个子树
            else:
                # 将节点的左右子树存入结果中，其中flag设置为false，表示存入的是树而非值
                # 前序遍历的顺序是左－根－右，所以用栈时按照右－根－左的顺序存储
                if cur.right:
                    st.append((cur.right,False))
                # 将节点存回st中
                st.append((cur,True))
                if cur.left:
                    st.append((cur.left,False))
        return res

