"""
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    通过使用具有 不同速度 的快、慢两个指针遍历链表，空间复杂度可以被降低至 O(1)
    慢指针每次移动一步，而快指针每次移动两步，如果存在环，则快指针会追到慢指针
结果：
    执行用时 : 44 ms, 在所有 Python3 提交中击败了92.35%的用户
    内存消耗 : 18.1 MB, 在所有 Python3 提交中击败了32.48%的用户
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False