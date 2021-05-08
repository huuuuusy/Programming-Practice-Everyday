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
    执行用时 : 204 ms, 在所有 Python3 提交中击败了34.01%的用户
    内存消耗 : 17.9 MB, 在所有 Python3 提交中击败了9.24%的用户
"""

# 定义链表
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None 

class Solution:
    def mergeKLists(self, lists):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # nodes用于存储所有的节点值
        nodes = []
        head = point = ListNode(0)
        # 遍历lists所有的链表
        for l in lists:
            # 当前链表非空时，存储当前链表的所有元素
            while l:
                nodes.append(l.val)
                l = l.next
        # 遍历排序后的nodes,从中取出所有的值存入point
        # head.next指向point的头结点
        for node in sorted(nodes):
            point.next = ListNode(node)
            point = point.next
        return head.next

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3 = ListNode(2)
    l3.next = ListNode(6)
    lists = [l1, l2, l3]
    res = Solution().mergeKLists(lists)
    while res:
        print(res.val)
        res = res.next