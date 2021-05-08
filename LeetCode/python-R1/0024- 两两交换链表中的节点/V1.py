"""
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    暴力解法，直接取出所有元素，排序后再存入新的链表中
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了76.77%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.93%的用户
"""

# 定义链表
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None 

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        point = head
        # 排除特殊情况
        if head is None or head.next is None:
            return head
        while head:
            # 正常情况：两两交换
            if head.next.next is not None:
                head.val, head.next.val = head.next.val, head.val
                head = head.next.next
            # 奇数个节点时
            if head.next is not None and head.next.next is None:
                head.val, head.next.val = head.next.val, head.val
                return point
            if head.next is None:
                return point

            


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next = ListNode(6)
    head = l1
    res = Solution().swapPairs(head)
    while res:
        print(res.val)
        res = res.next