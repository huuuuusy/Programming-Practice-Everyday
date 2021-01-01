""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code
工具： python3
"""

"""
实验11-1：首先创建一个叫做 Person 的类，然后创建两个派生类 Student 和 Teacher。当两个类都从 Person 类继承时，它们的类除了会有 Person 类的所有方法还会有自身用途的新方法和新变量。
"""
#!/usr/bin/env python3
import sys
from collections import Counter

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self):
        return 0


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year,grade):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        self.grade = grade

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):

        common = Counter(self.grade).most_common(4)
        n1 = 0
        n2 = 0
        for item in common:
            if item[0] != 'D':
                n1 += item[1]
            else:
                n2 += item[1]
        print("Pass: {}, Fail: {}".format(n1,n2))

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers, grade):
        Person.__init__(self, name)
        self.papers = papers
        self.grade = grade

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        s = []
        common = Counter(self.grade).most_common(4)
        for i,j in common:
            s.append("{}: {}".format(i,j))
        print(', '.join(s))

person1 = Person('Sachin')
if sys.argv[1] == "student":
    student1 = Student('Kushal', 'CSE', 2005, sys.argv[2])
    student1.get_grade()
else:
    teacher1 = Teacher('Prashad', ['C', 'C++'], sys.argv[2])
    teacher1.get_grade()