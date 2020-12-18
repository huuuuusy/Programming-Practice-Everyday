""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
介绍： 用Python3构建二叉树并完成相关操作函数的编写
"""

import sys
import string

"""
二叉树定义
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

"""
插入
    在二叉搜索树插入一个键k时：
        如果树为空，创建一个叶子节点，使key=key
        如果k小于根节点的key,将其插入左子树
        如果k大于根节点的key,将其插入右子树
"""

