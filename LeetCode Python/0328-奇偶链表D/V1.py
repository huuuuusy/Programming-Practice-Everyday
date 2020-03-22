""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    两个节点p和q分别指向奇数节点的头节点和偶数节点的头结点
    t用来将最后的链表连接起来
结果：
    执行用时 : 60 ms, 在所有 Python3 提交中击败了90.89%的用户
    内存消耗 : 15 MB, 在所有 Python3 提交中击败了77.37%的用户
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        # p是指向奇数节点的头结点
        p = head
        # q是指向偶数节点的头结点
        t = q = head.next
        while p and q and q.next:
            p.next, q.next = p.next.next, q.next.next
            p, q = p.next, q.next
        # 将偶节点链表链接在最后一个奇数节点之后
        p.next = t
        return head








