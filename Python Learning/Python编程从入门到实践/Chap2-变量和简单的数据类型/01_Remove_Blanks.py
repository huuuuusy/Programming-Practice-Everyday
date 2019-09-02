""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
任务： 剔除人名中的空白
      存储一个人名，并在其开头和末尾都包含一些空白字符
      打印这个人名，以显示其开头和末尾的空白
      分别使用剔除函数lstrip（），rstrip（）对人名进行处理，并将结果打印出来
"""

name = "\tMartin Luther King\n"

print("Unmodified:\n", name)
print("Using lstrip():\n", name.lstrip())
print("Using rstrip():\n", name.rstrip())
print("Using strip():\n", name.strip())
