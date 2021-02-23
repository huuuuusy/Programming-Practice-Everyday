"""
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    递归
参考：
    https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/chao-qiang-gifzhu-ni-li-jie-shi-yong-di-gui-fa-qiu/
结果：
    执行用时 : 64 ms, 在所有 Python3 提交中击败了17.44%的用户
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
        if head == None or head.next == None:
            return head

        l1 = head.next
        head.next = self.swapPairs(head.next.next)
        l1.next = head

        return l1

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