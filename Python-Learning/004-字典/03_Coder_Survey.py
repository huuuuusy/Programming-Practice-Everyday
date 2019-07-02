""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

任务：调查编程人员喜欢的语言，打印每个人喜欢的语言
1. 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中
2. 遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢
   对于还未参与调查的人，打印一条消息邀请他参与调查
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

print("\n")

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']

for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")