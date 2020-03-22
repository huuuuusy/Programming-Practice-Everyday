"""
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    直接解法，利用哑结点构建链表，比较两个有序链表的值的大小，决定链接的顺序
结果：
    执行用时 : 80 ms, 在所有 Python3 提交中击败了14.85%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了5.66%的用户
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 先添加一个哑节点
        dummy = ListNode(0)
        p = dummy
        while l1 or l2:
            # 当l1和l2都有元素时
            if l1 and l2:
                tmp1 = l1
                tmp2 = l2
                # 比较l1和l2的元素大小，p链接值较小的元素
                if tmp1.val < tmp2.val:
                    p.next = tmp1
                    l1 = l1.next
                else:
                    p.next = tmp2
                    l2 = l2.next
            # 如果只剩下l1有元素，则将l1剩下的元素链接
            elif l1:
                p.next = l1
                l1 = l1.next
            # 如果只剩下l2有元素，则将l2剩下的元素链接
            elif l2:
                p.next = l2
                l2 = l2.next
            p = p.next
        # 返回哑结点的下一个元素
        return dummy.next


        
        
        


