""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 
工具： python == 3.7.6
介绍： 深度之眼《Python高手之路》项目实战2：电子商城
"""

# settings.py为配置文件

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__)) # 两层dirname嵌套是因为settings.py文件是在conf文件夹内而非直接放在主目录下，所以需要多一层退出conf文件夹
BASE_DB = os.path.join(BASE_DIR, 'db')
BASE_LOG = os.path.join(BASE_DIR, 'log')



