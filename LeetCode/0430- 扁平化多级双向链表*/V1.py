""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    根据扁平化的链表的节点顺序，发现非常类似栈的数据结构，因此可以用栈保存每个节点的下一节点和子节点
    然后根据后进先出的原则依次弹出，并链接进链表中
结果：
    执行用时 : 1352 ms, 在所有 Python3 提交中击败了10.7%的用户
    内存消耗 : 336 MB, 在所有 Python3 提交中击败了5.89%的用户
""" 

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # 构建栈,其中临时存当前节点的next节点和child节点
        stack = [head] if head else None
        # p是扁平化链表的指针
        p = None
        # 从栈中读取数据
        while stack:
            # 当前处理的节点是栈中的最后一个接待
            node = stack.pop()
            # 将当前节点的下一个节点和子节点放到栈中，根据后入先出原则，有子节点的将优先弹出子节点
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
            # 将当前元素链接进最后的结果
            if p:
                p.next = node
                node.prev = p
                p.child = node.child = None
            p = node
        return head
        