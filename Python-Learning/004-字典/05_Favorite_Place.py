""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

任务：
1. 创建一个名为favorite_places的字典
2. 在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的1-3个地方
3. 遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来
"""

favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'ever': ['mt. verstovia', 'the playground', 'south carolina']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + "likes the following places:")
    for place in places:
        print(place.title())