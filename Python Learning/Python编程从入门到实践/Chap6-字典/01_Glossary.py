""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
任务： 1. 想5个词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中
      2. 以整洁的方式打印每个词汇及其含义
"""

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)