"""
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    递归的思想，两个链表头部较小的一个与剩下元素的 merge 操作结果合并
    我们直接将以上递归过程建模，首先考虑边界情况
    特殊的，如果 l1 或者 l2 一开始就是 null ，那么没有任何操作需要合并，所以我们只需要返回非空链表
    否则，我们要判断 l1 和 l2 哪一个的头元素更小，然后递归地决定下一个添加到结果里的值
    如果两个链表都是空的，那么过程终止，所以递归过程最终一定会终止
结果：
    执行用时 : 64 ms, 在所有 Python3 提交中击败了39.76%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了5.66%的用户
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 先排除空链表的情况
        if not l1:
            return l2
        if not l2:
            return l1
        # 如果l1的当前值小，则list1[0]+merge(list1[1:],list2)
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        # 如果l2的当前值小，则list2[0]+merge(list1,list2[1:])
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
            


        
        
        


