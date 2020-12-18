""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
任务： 在01_Restaurant基础上
        1. 添加一个名为number_served的属性，并将其默认值设置为0
        根据这个类创建一个名为restaurant的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它
        2. 添加一个名为set_number_served()的方法，它让你能够设置就餐人数
        调用这个方法并向它传递一个值，然后再次打印这个值
        3. 添加一个名为increment_number_served()的方法，它让你能够增加就餐人数
        调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数 
"""

class Restaurant():
    # 初始化餐馆
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    # 显示餐馆信息
    def describe_restaurant(self):
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)
    
    # 显示餐馆正在营业
    def open_restaurant(self):
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)
    
    # 设置用餐人数
    def set_number_served(self, number_served):
        self.number_served = number_served

    # 增加用餐人数
    def increment_number_served(self, additional_served):
        self.number_served += additional_served
    
restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))

