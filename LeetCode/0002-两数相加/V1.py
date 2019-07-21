""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
"""

"""
思路：
    直接求解，先转化为数值进行计算，再换成链表
结果：
    执行用时 : 108 ms, 在所有 Python3 提交中击败了47.86%的用户
    内存消耗 : 14 MB, 在所有 Python3 提交中击败了5.06%的用户
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 用num1和num2保存数字
        num1 = []
        num2 = []
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        for i in range(len(num1)):
            num1[i] = str(num1[i])
        # 用tmp1和tmp2将数字倒序 
        tmp1 = "".join(num1[::-1])
        for i in range(len(num2)):
            num2[i] = str(num2[i]) 
        tmp2 = "".join(num2[::-1])
        tmp = int(tmp1) + int(tmp2)
        # num保存计算结果
        num = list(str(tmp))[::-1]
        # 构造新的链表，存储结果      
        for i in range(len(num)):
            num[i] = int(num[i])
        p = ListNode(num[0])
        head = p
        for i in num[1:]:
            p.next = ListNode(i)
            p = p.next
        return head
