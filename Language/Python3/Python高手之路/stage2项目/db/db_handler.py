""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 
工具： python == 3.7.6
介绍： 深度之眼《Python高手之路》项目实战2：电子商城
"""

# db_handler为数据库相关操作文件

def select(name):
    # 依据name选取用户的json文件
    user_path = os.path.join(setting.BASE_DB, '%s.json'%name)
    if os.path.exists(name):
        with open(user_path, mode='r', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic
        else:
            return None
        
def save(user_dic):
    # 保存最新的用户json文件
    user_path = os.path.join