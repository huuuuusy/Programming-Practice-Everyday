"""
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    分配一个 Set 去保存所有的列表节点，我们逐一遍历列表，检查当前节点是否出现过
    如果节点已经出现过，那么一定形成了环且它是环的入口
    否则如果有其他点是环的入口，我们应该先访问到其他节点而不是这个节点
    其他情况，没有成环则直接返回 null 
    如果 while 循环终止，我们返回 null 因为我们已经将所有的节点遍历了一遍且没有遇到重复的节点，这种情况下，列表是不成环的。
    对于循环列表， while 循环永远不会停止，但在某个节点上， if 条件会被满足并导致函数的退出
结果：
    执行用时 : 44 ms, 在所有 Python3 提交中击败了94.72%的用户
    内存消耗 : 18.7 MB, 在所有 Python3 提交中击败了7.25%的用户
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None
        