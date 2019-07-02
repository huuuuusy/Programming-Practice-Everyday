""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

任务：
1. 创建一个名为Restaurant类，其方法__init__()设置两个属性：restaurant_name和cuisine_type
2. 创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业
3. 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法
"""

class Restaurant():
    # 初始化餐馆
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
    
    # 显示餐馆信息
    def describe_restaurant(self):
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)
    
    # 显示餐馆正在营业
    def open_restaurant(self):
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)
    
restaurant = Restaurant('the mean queen', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

