""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 
工具： python == 3.7.6
介绍： 深度之眼《Python高手之路》作业06：函数概述
"""

"""
练习一
写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成修改操作
"""
import os
def modify_file(file_name, old_content, new_content):
    with open(file_name, mode='rt', encoding='utf-8') as read_f, \
        open('%s.swap'%file_name, mode='wt', encoding='utf-8') as write_f:
        for line in read_f:
            if old_content in line:
                line = line.replace(old_content, new_content)
            write_f.write(line)
    os.remove(file_name)
    os.rename('%s.swap'%file_name, file_name)

"""
练习二
写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
"""
def calculate_count(data_str):
    dict_count = {'alpha': 0, 'number': 0, 'space': 0, 'other': 0}
    for i in data_str:
        if i.isalpha():
            dict_count['alpha'] += 1
        elif i.isdigit():
            dict_count['number'] += 1
        elif i is ' ':
            dict_count['space'] += 1
        else:
            dict_count['other'] += 1
    print(dict_count)

"""
练习三
写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
"""    
def judge_length(data):
    return True if len(data)>5 else False

"""
练习四
写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
"""    
def check_up_list(data_list):
    return data_list[:2] if len(data_list)>2 else False

"""
练习五
写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
"""
def get_odd_list(data):
    odd_list = []
    for i in range(len(data)):
        if i%2 == 0:
            odd_list.append(data[i])
    return odd_list

"""
练习六
写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dict1 = {"k1": "v1v1", "k2": [11, 22, 33, 44], 'k3': (9, 8, 7, 65, 4)}
"""
def check_length_list(data_dict):
    for k, v in data_dict.items():
        if len(v) > 2:
            data_dict[k] = v[:2]
    return data_dict
            
if __name__ == '__main__':
    #modify_file('db.txt', '001', '001[yes]')
    #calculate_count('32441adhjf ^&%$#@()*')
    #print(judge_length('sahdlfk'))
    #print(check_up_list([1, 2, 3, 4, 4, 5, ]))
    #print(get_odd_list([1, 2, 3, 4, ]))
    dict1 = {"k1": "v1v1", "k2": [11, 22, 33, 44], 'k3': (9, 8, 7, 65, 4)}
    print(check_length_list(dict1))
