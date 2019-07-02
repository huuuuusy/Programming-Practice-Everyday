""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

任务：
编写一个程序，调查用户梦想的度假胜地,使用字典存储数据
使用类似于“If you could visit one place in the world, where would you go?”的提示，并编写一个打印调查结果的代码块
"""

name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

responses = {}

while True:
    # 询问用户想去哪度假
    name = input(name_prompt)
    place = input(place_prompt)

    # 存储调查结果
    responses[name] = place

    # 询问是否还有其他人要参与调查。
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break
    
# 显示调查结果。
print("\n--- Results ---")
for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")