""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

任务：
1. 创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会存储的其他几个属性
2. 在类User中定义一个名为describe_user()的方法，它打印用户信息摘要
再定义一个名为greet_user()的方法，它向用户发出个性化的问候
3. 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法
"""

class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
    
    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)
    
    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")
    
eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()