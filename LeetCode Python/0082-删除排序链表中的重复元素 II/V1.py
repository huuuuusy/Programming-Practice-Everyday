""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    用数组辅助，然后再重新构建链表
结果：
    执行用时 : 88 ms, 在所有 Python3 提交中击败了21.81%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.4%的用户
""" 

# 定义链表
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None 

class Solution:
    def deleteDuplicates(self, head):
        # 辅助列表
        nums = []
        remove = []
        point = head
        # 先将所有元素存储到两个辅助列表中
        while point:
            if point.val in nums:
                remove.append(point.val)
            nums.append(point.val)
            point = point.next
        head = point = ListNode(0)
        # 再重新构建新的链表
        for num in nums:
            if num not in remove:
                point.next = ListNode(num)
                point = point.next
        return head.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(1)
    #l1.next.next = ListNode(3)
    #l1.next.next.next = ListNode(3)
    #l1.next.next.next.next = ListNode(4)
    #l1.next.next.next.next.next = ListNode(4)
    #l1.next.next.next.next.next.next = ListNode(5)
    head = l1
    res = Solution().deleteDuplicates(head)
    while res:
        print(res.val)
        res = res.next