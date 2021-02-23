""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路：
    掌握链表数据结构的特点
结果：
    执行用时 : 124 ms, 在所有 Python3 提交中击败了28.86%的用户
    内存消耗 : 13.8 MB, 在所有 Python3 提交中击败了5.06%的用户
"""

# 定义链表
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None 

class Solution:
    def addTwoNumbers(self,l1,l2):
        head = ListNode(0)
        p = head
        quot = 0
        while l1 or l2 or quot !=0:
            if l1: 
                quot += l1.val
                l1 = l1.next
            if l2: 
                quot += l2.val
                l2 = l2.next
            quot, rem = divmod(quot,10) # divmod()函数分别返回整除的结果和取余数的结果
            # 整除的结果作为进位存到下一轮
            # 将余数存储到p.next()中
            p.next = ListNode(rem)
            p = p.next
        return head.next
    
def compareLinkedList(l1, l2):
    """
    比较两个链表是否相等
    """
    while l1 or l2:
        if not (l1 and l2) or l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return True

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    lsum = ListNode(7)
    lsum.next = ListNode(0)
    lsum.next.next = ListNode(8)
    # 比较两个链表相加的结果是否和sum相等
    print(compareLinkedList(Solution().addTwoNumbers(l1, l2), lsum))