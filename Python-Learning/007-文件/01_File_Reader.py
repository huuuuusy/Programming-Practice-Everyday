""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

任务：
读取指定文件，并打印文件内容
"""

filename = 'data/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
