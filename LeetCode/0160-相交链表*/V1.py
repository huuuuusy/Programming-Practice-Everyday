"""
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    换个消除长度差的方式：拼接两链表。 
    设长-短链表为 C ，短-长链表为 D ，则当 C 走到长短链表交接处时， D 走在长链表中，且与长链表头距离为 长度差;
链接：
    https://leetcode-cn.com/problems/two-sum/solution/intersection-of-two-linked-lists-shuang-zhi-zhen-l/
结果：
    执行用时 : 240 ms, 在所有 Python3 提交中击败了81.03%的用户
    内存消耗 : 41.8 MB, 在所有 Python3 提交中击败了30.4%的用户
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 最开始ha,hb在两个链表的头节点
        ha = headA
        hb = headB
        # 如果两个节点不同
        while ha != hb:
            # ha将继续向后进行，直到链表A被遍历完，然后ha开始遍历链表B
            # hb同理
            # 这一操作类似于进行拼接
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        # 最终返回ha(此时ha=hb，是相交点)
        return ha
        
        