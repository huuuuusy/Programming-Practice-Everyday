""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

任务：
编写一个函数，将一辆汽车的信息存储在一个字典中
这个函数总是接受制造商和型号，还接受任意数量的关键字实参
"""

def make_car(manufacturer, model, **options):
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }
    for option, value in options.items():
        car_dict[option] = value
    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_accord)  