""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
任务： 以附加模式将内容写进空白文件
"""

filename = 'data/programming.txt'

# 'a'是附加模式，即在原有内容后面写进新内容
# 'w'是写入模式，将清空原有文件内容后写入新内容
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
