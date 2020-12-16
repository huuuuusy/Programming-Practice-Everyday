""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code
工具： python3
"""

"""
实验6-1:输入学生数量，以及各个学生物理、数学、历史三科的成绩，如果总成绩小于 120，程序打印 “failed”，否则打印 “passed”。
"""
#!/usr/bin/env python3
n = int(input("Enter the number of students: "))
data = {} # 用来存储数据的字典变量
Subjects = ('Physics', 'Maths', 'History') # 所有科目
for i in range(0, n):
    name = input('Enter the name of the student {}: '.format(i + 1)) # 获得学生名称
    marks = []
    for x in Subjects:
        marks.append(int(input('Enter marks of {}: '.format(x)))) # 获得每一科的分数
    data[name] = marks
for x, y in data.items():
    total =  sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 120:
        print(x, "failed :(")
    else:
        print(x, "passed :)")
