""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    测试用例有问题，用python自带的集合解题
结果：
    执行用时 : 284 ms, 在所有 Python3 提交中击败了24.62%的用户
    内存消耗 : 18.6 MB, 在所有 Python3 提交中击败了53.62%的用户
"""

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr=[-1]*100000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.arr[key]=value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
  
        return self.arr[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.arr[key]=-1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)