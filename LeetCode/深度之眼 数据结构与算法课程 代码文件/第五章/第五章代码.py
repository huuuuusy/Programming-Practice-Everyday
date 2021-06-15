#硬币
import random
rand = random.sample(range(1,100),10)

def goldCoin(current):
    return current * rand[current-1]

def totalCoin(n):
    total = 0
    for i in range(1,n+1):
        coin = goldCoin(i)
        total = total + coin
return total

print(totalCoin(10))

#阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

#青蛙跳台阶
def frog(n):
    if n == 1 :
        return 1
    elif n == 2:
        return 2
    else:
        return frog(n-1)+frog(n-2)

print(frog(7))

#斐波那契-递归
class Solution:
    def fib(self, N: int) -> int:
        # 初始化边界
        if N <= 1:
            return N
        return self.fib(N-1) + self.fib(N-2)
#斐波那契-记忆搜索
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:   #初始化边界
            return N
        self.cache = {0: 0, 1: 1}   
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        if N in self.cache.keys():   #遇到子问题先查备忘录，如果计算过，就不再计算了
            return self.cache[N]
        self.cache[N] = self.memoize(N-1) + self.memoize(N-2)
        return self.memoize(N)
#汉诺塔
def  Hanoi(n,first,second,third):
    if n==1:
        print(first+'-->'+third)
    else:
        Hanoi(n-1,first,third,second)
        print(first+'-->'+third)
        Hanoi(n-1,second,first,third)

Hanoi(3,'A','B','C')

#leetcode203
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None  
        head.next = self.removeElements(head.next,val)  #将该元素和后面所有元素分为两组递归
        return head.next if head.val == val else head 
