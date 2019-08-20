""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    用DFS递归检索
结果：
    执行用时 : 60 ms, 在所有 Python3 提交中击败了87.4%的用户
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
        lookup = {}
        # 构建DFS函数，递归调用
        def dfs(head):
            if not head:
                return None
            if head in lookup:
                return lookup[head]
            clone = Node(head.val, None, None)
            lookup[head] = clone
            clone.next, clone.random = dfs(head.next), dfs(head.random)
            return clone
        return dfs(head)
