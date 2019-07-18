""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    用p指向每一个元素，判断其是否满足删除的需求，如果满足则删除
结果：
    执行用时 : 84 ms, 在所有 Python3 提交中击败了98.61%的用户
    内存消耗 : 16.2 MB, 在所有 Python3 提交中击败了96.62%的用户
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None
        while head is not None and head.val == val:
            head = head.next
        if head == None:
            return None

        p = head

        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return head


        