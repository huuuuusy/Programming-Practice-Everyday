""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 
工具： python == 3.7.6
介绍： 深度之眼《Python高手之路》作业05：文件处理
"""

"""
练习一
写一个程序在要保持文件内容的顺序不变的前提下，去除文件中重复的行。
"""
import os
def hw1():
    with open('test.txt','r', encoding='utf-8') as read_f, \
        open('test.txt.swap', 'w', encoding='utf-8') as write_f:
        s = set()
        for line in read_f:
            if line not in s:
                s.add(line)
                write_f.write(line)
    os.remove('test.txt')
    os.rename('test.txt.swap', 'test.txt')
    
"""
练习三
写一个修改文件的程序，要求是原来的内容不能被覆盖，修改之后字符之间的空格不能变化（4个空格）
源文件内容如下：
马一特    18    male
刘德华    50    male
林志玲    20    female
修改后的文件：
马一特[Albert]    18    male
刘德华    50    male
林志玲    20    female
"""

def hw3():
    src = 'user.txt'
    swap = 'user.txt.swap'
    with open(src, mode='rt', encoding='utf-8') as read_f, \
        open(swap, mode='wt', encoding='utf-8') as write_f:
        for line in read_f:
            print(line)
            if '马一特' in line:
                line = line.replace('马一特', '马一特[Albert]')
            write_f.write(line)
    os.remove(src)
    os.rename(swap, src)


if __name__ == '__main__':
    #hw1()
    hw3()