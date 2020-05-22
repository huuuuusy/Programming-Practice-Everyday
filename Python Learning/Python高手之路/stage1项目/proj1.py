""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 
工具： python == 3.7.6
介绍： 深度之眼《Python高手之路》项目实战1-1：多级菜单
注意： 列表和多级菜单的配合以及while循环的终止条件
       利用append和pop实现层级选择
"""

"""
要求：
    打印三级菜单如：汽车，种类，品牌，型号，可以自由发挥 
    可返回上一级
    可随时退出程序
"""
def proj(menu):
    layers = [menu]
    while True:
        # 空白菜单不打印
        if len(layers) == 0:
            print('Error, empty menu!')
            break
        current_layer = layers[-1]
        
        for key in current_layer:
            print(key)
        
        choice = input('>>: ').strip()
        # 若已经进入子层，输入b可以将layers列表的最后一项弹出，相当于退出一层
        if choice == 'b':
            layers.pop(-1)

        if choice == 'q':
            break

        if choice not in current_layer:
            continue
        
        # 在layers列表中添加输入的key及其包含的字典内容
        layers.append(current_layer[choice])
        

if __name__ == '__main__':
    menu = {
        '汽车': {
            '轿车': {
                '宝马': {
                    '宝马760': {},
                    '宝马M5': {},
                    '宝马M3': {}
                },
                '奔驰': {
                    '奔驰C180': {},
                    '奔驰E260': {},
                    '奔驰S600': {},
                },
                '奥迪': {
                    '奥迪A4L': {},
                },
            },
            '越野车': {
                '保时捷': {
                    '保时捷Macan': {},
                    '保时捷Cayenne': {},
                },
                '路虎': {},
                '英菲尼迪': {},
            },
            '卡车': {},
            '公交车': {},
        },
        '飞机': {
            '大飞机': {
                "大1": {
                    'xxx': {}
                }
            },
            '小飞机': {
                '小1': {
                    'xxx': {}
                }
            },
            '直升机': {},
        },
        '大炮': {}
    }
    proj(menu)