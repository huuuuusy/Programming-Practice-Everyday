""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    直接计算，因为是有序链表，所以可以直接比较当前两个元素的值是否相同
结果：
    执行用时 : 64 ms, 在所有 Python3 提交中击败了72.13%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了5.01%的用户
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 排除特殊情况
        if head == None or head.next == None:
            return head
        p = head
        # 比较当前相邻元素的值是否相同
        while p:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
            if p.next == None:
                break
        return head