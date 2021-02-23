"""
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    用栈，把 k 个数压入栈中，然后弹出来的顺序就是翻转的
注意：
    第一，剩下的链表个数够不够 k 个（因为不够 k 个不用翻转）
    第二，已经翻转的部分要与剩下链表连接起来
链接：
    https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/kge-yi-zu-fan-zhuan-lian-biao-by-powcai/
结果：
    执行用时 : 92 ms, 在所有 Python3 提交中击败了24.77%的用户
    内存消耗 : 14.6 MB, 在所有 Python3 提交中击败了11.93%的用户
"""

# 定义链表
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None 

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 添加一个哑结点在头部
        dummy = ListNode(0)
        p = dummy
        while True:
            count = k
            # 使用栈
            stack = []
            tmp = head
            # 将数据压入栈中
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            # 此时tmp在k+1的位置
            # 剩下的链表不够k个，跳出循环
            if count: 
                p.next = head
                break
            # 翻转
            while stack:
                p.next = stack.pop()
                p = p.next
            # 与剩下的链表连接
            p.next = tmp
            head = tmp        
        return dummy.next
            
if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    #l1.next.next.next.next.next = ListNode(6)
    head = l1
    k = 2
    res = Solution().reverseKGroup(head, k)
    while res:
        print(res.val)
        res = res.next