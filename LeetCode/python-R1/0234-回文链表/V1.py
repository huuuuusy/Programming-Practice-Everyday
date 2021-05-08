""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    用列表存储链表元素，并翻转后半列表进行判断
注意：
    空链表也是回文链表
结果：
    执行用时 : 88 ms, 在所有 Python3 提交中击败了95.25%的用户
    内存消耗 : 24.1 MB, 在所有 Python3 提交中击败了12.28%的用户
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 如果是空链表或者只有一个头结点的链表，则是回文链表
        if head == None or head.next == None:
            return True
        # 保存链表节点值
        target = []
        while head:
            target.append(head.val)
            head=head.next
        # p,q分别指向中间的两个元素
        p = (len(target)-1)//2+1
        q = (len(target))//2
        
        return target[0:p]==target[q:len(target)][::-1]








