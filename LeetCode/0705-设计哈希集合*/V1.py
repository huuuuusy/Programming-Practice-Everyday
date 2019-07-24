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
    执行用时 : 212 ms, 在所有 Python3 提交中击败了44.56%的用户
    内存消耗 : 18.7 MB, 在所有 Python3 提交中击败了41.97%的用户
"""

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set([])

    def add(self, key: int) -> None:
        self.set.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.set
    

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)