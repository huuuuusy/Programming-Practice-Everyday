
#leetcode 203
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        p = dummy

        while p.next != None:
            # 当前值等于val，跳过，p指针不移动
            if p.next.val == val:
                p.next = p.next.next
            # 当前值不等于val，p指针后移
            else:
                p = p.next

        return dummy.next

#leetcode 237
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


# leetcode 86
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 创建两个链表，分别保存小于x的数、大于等于x的数
        cur = head

        l1 = ListNode(0)
        l2 = ListNode(0)
        head1 = l1
        head2 = l2

        while cur != None:
            if cur.val < x:
                l1.next = ListNode(cur.val)
                l1 = l1.next
            else:
                l2.next = ListNode(cur.val)
                l2 = l2.next
            cur = cur.next
        
        # 两个链表拼接在一起
        l1.next = head2.next

        return head1.next
#leetcode 24
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 创建头节点
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        a = dummy
        b = dummy

        while pre.next != None and pre.next.next != None:
            a = pre.next
            b = pre.next.next
            pre.next = b
            a.next = b.next
            b.next = a
            pre = pre.next.next
        
        return dummy.next

#leetcode 143
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        
        # 循环找到链表末尾
        n = 1
        cur = head
        while cur.next != None:
            cur = cur.next
            n += 1

        # 链表末尾连接到链表头
        cur.next = head

        # 循环找到链表第k个节点（拆分处）
        end = head
        for _ in range(n-k%n-1):
            end = end.next
        
        # 断开第k个节点
        new_head = end.next
        end.next = None

        return new_head

#leetcode 61
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return head

        # 第1遍扫描，找到中点
        fast = head
        slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow

        # 第2遍扫描，将后半段的指针都反向
        a = mid.next
        b = a.next
        mid.next = None
        a.next = None

        while b:
            t = b.next
            b.next = a
            a = b
            b = t

        # 第3遍扫描，将后半段交替插入前半段
        b = head
        while a:
            t = a.next
            a.next = b.next
            b.next = a
            b = b.next.next
            a = t

        return head

#leetcode 206
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head

        while cur != None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre

#leetcode 92
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 初始化pre、cur
        pre = None
        cur = head

        # cur 指针抵达第 m 个结点
        while m > 1:
            pre = cur
            cur = cur.next
            m -= 1
            n -= 1

        # 初始化con、tail
        con = pre
        tail = cur

        # 链表反转
        while n > 0:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            n -= 1

        # con、tail链接调整
        if con:
            con.next = pre
        else:
            head = pre
        tail.next = cur

        return head
#leetcode 25
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        dummy = ListNode(0)
        dummy.next = head

        l_old = dummy
        end = dummy
        start = head

        while True:
            # k次循环，end到达一组的末尾
            for _ in range(k):
                end = end.next
                if end == None:
                    break

            # 链表到达末尾（剩余不够k个）
            if end == None:
                break

            # 分割开后面的链表
            l_new = end.next
            end.next = None
            # 反转这k个链表（返回的是反转后的头节点）
            temp = self.reverse(start)
            # 前面部分已反转完成的链表接上这个头节点
            l_old.next = temp
            # 更新这几个指针
            l_old = start
            end = start
            start.next = l_new
            start = start.next

        return dummy.next


    # 反转链表
    def reverse(self, head):
        dummy = ListNode(0)
        pre = dummy
        cur = head

        while cur != None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre


#leetcode 19
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 设置头节点，简化某些极端情况，例如列表中只含有一个结点，或需要删除列表的头部。
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        # 快指针先走n+1步
        for _ in range(n+1):
            fast = fast.next

        # 两个指针一起移动，直到快指针到达None
        while fast != None:
            slow = slow.next
            fast = fast.next

        # 删除慢指针指向的节点，也就是倒数第n个节点
        slow.next = slow.next.next

        return dummy.next

#leetcode 83
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else: cur = cur.next

        return head
#leetcode 82
class Solution(object):
    def deleteDuplicates(self, head):
        if not (head and head.next):
            return head
        dummy = ListNode(0)
        dummy.next = head
        a = dummy
        b = head
        while b and b.next:
            # 初始化的时a指向的是哑结点，所以比较逻辑应该是a的下一个节点和b的下一个节点
            if a.next.val!=b.next.val:
                a = a.next
                b = b.next
            else:
                # 如果a、b指向的节点值相等，就不断移动b，直到a、b指向的值不相等 
                while b and b.next and a.next.val==b.next.val:
                    b = b.next
                a.next = b.next
                b = b.next
        return dummy.next

#leetcode 141
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

#leetcode 142 
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        while True:
            # 链表无环
            if fast.next == None or fast.next.next == None:
                return None
            slow = slow.next
            fast = fast.next.next
            # 双指针第一次相遇
            if slow == fast:
                break

        # 构造第二次相遇
        fast = dummy
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
#两个链表相交的一系列问题
#问题一
#python3.5
def getLoopNode(head):
    if head == None or head.next == None or head.next.next == None:
        return None
    slow = head.next
    fast = head.next.next
    while slow != fast:
        if fast.next == None or fast.next.next == None:
            return None
        slow = slow.next
        fast = fast.next.next
    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
#问题二
def noLoop(head1, head2):
    if head1 == None or head2 == None:
        return None
    cur1 = head1
    cur2 = head2
    n = 0
    while cur1.next != None:
        n += 1
        cur1 = cur1.next
    while cur2.next != None :
        n -= 1
        cur2 = cur2.next
    if cur1 != cur2:
        return None 
    cur1 = head1 if n >= 0 else head2
    cur2 = head1 if cur1 == head2 else head2
    n = abs(n)
    while n != 0:
        cur1 = cur1.next 
        n -= 1
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1
#问题三：
def bothLoop(head1, node1, head2, node2):
    if head1 == None or head2 == None:
        return None
    if node1 == node2:
        cur1 = head1
        cur2 = head2
        n = 0
        while cur1 != node1:
            n += 1
            cur1 = cur1.next
        while cur2 != node1:
            n -= 1
            cur2 = cur2.next
        cur1 = head1 if n >= 0 else head2
        cur2 = head1 if cur1 == head2 else head2
        n = abs(n)
        while n != 0:
            n -= 1
            cur1 = cur1.next
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:
        cur1 = node1.next
        while cur1 != node1:
            if cur1 == node2:
                return node1
            cur1 = cur1.next
        return None
#主函数
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def getIntersectNode(head1, head2):
    if head1 == None or head2 == None:
        return None
    node1 = getLoopNode(head1)
    node2 = getLoopNode(head2)
    if node1 == None and node2 == None:
        return noLoop(head1, head2)
    if node1 != None and node2 != None:
        return bothNode(head1, node1, head2, node2)
    return None





#leetcode 234
class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result    

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

#leetcode 328
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 特殊情况处理
        if head == None or head.next == None:
            return head

        # 奇偶指针初始化
        odd = head
        even = head.next
        evenHead = even

        # 奇偶指针分离
        while even != None and even.next != None:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        
        # 奇数链表的尾指针指向偶数链表的头指针
        odd.next = evenHead

        return head
#leetcode 2
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 初始化结果链表
        cur = ListNode(0)
        head = cur
        
        carry = 0
        while l1 != None or l2 != None:
            # 如果一个链表较短则在前面补0
            if l1 == None:
                x1 = 0
            else:
                x1 = l1.val
                l1 = l1.next
            if l2 == None:
                x2 = 0
            else:
                x2 = l2.val
                l2 = l2.next

            # 每一位计算的同时需要考虑上一位的进位问题，而当前位计算结束后同样需要更新进位值
            sums = (x1 + x2 + carry)%10
            carry = (x1 + x2 + carry)//10
            cur.next = ListNode(sums)
            cur = cur.next

        # 如果两个链表全部遍历完毕后，进位值为 1，则在新链表最前方添加节点 1
        if carry == 1:
            cur.next = ListNode(carry)

        return head.next