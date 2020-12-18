""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code
工具： python3
"""

"""
实验7-1:回文是一种无论从左还是从右读都一样的字符序列。比如 “madam”。在这个例子中，我们检查用户输入的字符串是否是回文，并输出结果。
"""
#!/usr/bin/env python3
s = input("Please enter a string: ")
z = s[::-1]  #把输入的字符串s 进行倒序处理形成新的字符串z
if s == z:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")