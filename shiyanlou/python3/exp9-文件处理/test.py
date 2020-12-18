""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code
工具： python3
"""

"""
实验9-1:文件读取
"""
#!/usr/bin/env python3
name = input("Enter the file name: ")
fobj = open(name)
print(fobj.read())
fobj.close()