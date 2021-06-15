 
#有效的括号
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        for ch in s:
            if ch in ['(','[','{']:
                stack.append(ch)
            
            else:
                if stack:
                    left = stack.pop()
                else:
                    return False
                if left=='[' and ch ==']' or left=='(' and ch==')' or left=='{' and ch=='}':
                    continue
                else:
                    return False
        if stack == []:
            return True
        else:
            return False






#四则运算表达式
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
 
        for s in tokens:
            if s in ['+','-','*','/']:
                b = stack.pop()
                a = stack.pop()
                if s == '+':
                    stack.append(a+b)
                elif s == '-':
                    stack.append(a-b)
                elif s == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(s))
                    
        ans = int(stack.pop())
        return ans








#设计一个有getMin功能的栈-方法1
class NewStack1:
    def __init__(self):
        self.stackData = []
        self.stackMin = []

    def push(self, newNum):
        self.stackData.append(newNum)
        if len(self.stackMin) == 0 or newNum <= self.getMin():
            self.stackMin.append(newNum)

    def pop(self):
        if len(self.stackData) == 0:
            raise Exception("stack is empty!")
        value = self.stackData.pop()
        if self.getMin() == value:
            self.stackMin.pop()
        return value

    def getMin(self):
        if len(self.stackMin) == 0:
            raise Exception("stack is empty!")
        return self.stackMin[-1]




#设计一个有getMin功能的栈-方法2
class NewStack2:
    def __init__(self):
        self.stackData = []
        self.stackMin = []

    def push(self, newNum):
        self.stackData.append(newNum)
        if len(self.stackMin) == 0 or newNum < self.getMin():
            self.stackMin.append(newNum)
        else:
            self.stackMin.append(self.getMin())

    def pop(self):
        if len(self.stackData) == 0:
            raise Exception("Stack is empty!")
        self.stackMin.pop()
        return self.stackData.pop()

    def getMin(self):
        if len(self.stackMin) == 0:
            raise Exception("Stack is empty!")
        return self.stackMin[-1]

#回文词检测

def palchecker(aString):

    deque = Deque()
    # 回文词入队
    for i in aString:
        deque.add_front(i)

    state = True
    # 双向读取并比较
    while deque.size() > 1 and state:
        df = deque.remove_front()
        dr = deque.remove_rear()
        # print(df,dr)
        if df != dr:
            state = False

    return state


#leetcode 232
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._s1, self._s2 = [], []
        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while self._s1:
            self._s2.append(self._s1.pop())  
        self._s1.append(x)
        while self._s2:
            self._s1.append(self._s2.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self._s1.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self._s1[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self._s1

#生成窗口最大数组
def getMaxWindow(arr, w):
    if arr == None or w < 1 or len(arr) < w:
        return
    qmax = []
    res = []
    for i in range(len(arr)):
        while qmax and arr[qmax[-1]] <= arr[i]:
            qmax.pop()
        qmax.append(i)
        if qmax[0] <= i - w:
            qmax.pop(0)
        if i-w+1 >= 0:
            res.append(arr[qmax[0]])
    return res
