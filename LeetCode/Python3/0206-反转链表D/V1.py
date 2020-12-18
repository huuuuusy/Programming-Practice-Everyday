""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    遍历链表，在遍历的过程中更新两个指针pre, head：
        pre, head分别指向前一个Node和当前Node，每次执行head.next = pre
        nex用于提前保存下一个Node。
    由于需要返回新的链表头部，所以设置跳出条件为head.next == null,跳出后将最后head指向pre，并返回head。
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了88.27%的用户
    内存消耗 : 14.6 MB, 在所有 Python3 提交中击败了26.69%的用户
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        if not head: return
        pre = None
        while head.next:
            nex = head.next
            head.next = pre
            pre = head
            head = nex
        head.next = pre
        return head
