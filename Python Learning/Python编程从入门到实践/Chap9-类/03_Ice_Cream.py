""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
任务： 在02_Restaurant_V2基础上
        1. 编写一个名为IceCreamStand的类，让它继承Restaurant类
        2. 添加一个名为flavors的属性，用于存储一个由各种口味的冰淇淋组成的列表
        3. 编写一个显示这些冰淇淋的方法
        4. 创建一个IceCreamStand实例，并调用这个方法
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
    
class IceCreamStand(Restaurant):
    def __iniit__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(flavor.title())
        
big_one = IceCreamStand('The Big One', 'ice_cream')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()