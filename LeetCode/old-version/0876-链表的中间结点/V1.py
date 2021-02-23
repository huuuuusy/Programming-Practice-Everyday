""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    直接搜索　
结果：
    执行用时 : 44 ms, 在所有 Python3 提交中击败了89.81%的用户
    内存消耗 : 14 MB, 在所有 Python3 提交中击败了5.22%的用户
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        num = []
        p = head
        while p:
            num.append(p.val)
            p = p.next
        # target计算中间节点的序号
        target = len(num)//2
        p = head
        # p确定中间节点
        for i in range(target):
            p = p.next 
        return p
        
