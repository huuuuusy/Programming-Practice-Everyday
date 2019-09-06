"""
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    使用快慢指针，快指针先移 n 个节点
    接下来，快慢指针一起移动，两指针之间一直保持 n 个节点
    当快指针到链表底了，操作慢指针，删除要删除的元素
结果：
    执行用时 : 28 ms, 在所有 Python3 提交中击败了71.58%的用户
    内存消耗 : 11.8 MB, 在所有 Python3 提交中击败了25.16%的用户
"""

# 定义链表
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None 

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return 
        # 先在头部添加一个哑结点
        dummy = ListNode(0)
        dummy.next = head
        # 让快指针从哑结点开始
        fast = dummy
        # 快指针移动n个节点
        while n:
            fast = fast.next
            n -= 1
        # 此时快慢指针相差n
        slow = dummy
        # 快慢指针开始一起移动
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        # 当快指针到达尾部时，慢指针指向待删除节点
        # 删除操作
        slow.next = slow.next.next
        # 返回删除后的链表
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    head = l1
    n = 2
    res = Solution().removeNthFromEnd(head, n)
    while res is not None:
        print(res.val)
        res = res.next