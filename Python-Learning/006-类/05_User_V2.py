""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

任务：在04_User的基础上
1. 添加一个名为login_attempts的属性
   编写一个名为increment_login_attempts()的方法，它将属性login_attempts的值加1
   再编写一个名为reset_login_attempts()的方法，它将属性login_ attempts的值重置为0
2. 根据User类创建一个实例，再调用方法increment_login_attempts()多次
   打印属性login_attempts的值，确认它被正确地递增
   然后，调用方法reset_login_attempts()，并再次打印属性login_attempts的值，确认它被重置为0
"""

class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0
    
    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)
    
    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
    
eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print("  Login attempts: " + str(eric.login_attempts))

print("Resetting login attempts...")
eric.reset_login_attempts()
print("  Login attempts: " + str(eric.login_attempts))