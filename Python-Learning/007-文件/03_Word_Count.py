""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

任务：
打开指定文本文档并确定文本的单词数量
"""

def word_count(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
    
filenames = ['data/alice.txt', 'data/siddhartha.txt']
for filename in filenames:
    word_count(filename)