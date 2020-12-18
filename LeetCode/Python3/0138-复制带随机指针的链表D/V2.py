""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    第一次循环是用字典存储所有的节点
    第二次循环是从字典中取出节点并链接
结果：
    执行用时 : 56 ms, 在所有 Python3 提交中击败了95.12%的用户
    内存消耗 : 16.2 MB, 在所有 Python3 提交中击败了5.33%的用户
""" 

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        lookup = {}
        node = head
        # 创建所有节点
        while node:
            lookup[node] = Node(node.val, None, None)
            node = node.next
        
        node = head
        # 节点连接
        while node:
            lookup[node].next = lookup.get(node.next)
            lookup[node].random = lookup.get(node.random)
            node = node.next
        
        return lookup[head]