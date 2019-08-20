""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    常规思路，用列表存储旋转变化的值，再重新构建链表
结果：
    执行用时 : 60 ms, 在所有 Python3 提交中击败了61.81%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了5.4%的用户
""" 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 排除特殊情况
        if not head:
            return None
        if k == 0:
            return head
        # nums存储节点的值
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        # 将nums旋转
        step = k%len(nums)
        nums = nums[-step:]+nums[:-step]
        # 根据旋转后的nums构建链表
        node = ListNode(nums[0])
        head = node
        for i in range(1,len(nums)):
            node.next = ListNode(nums[i])
            node = node.next
        return head

            



