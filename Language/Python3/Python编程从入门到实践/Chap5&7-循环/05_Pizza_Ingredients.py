""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
任务： 1. 编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit'时结束循环
      2. 每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料
"""

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break