import os
from conf import setting
import json


def save(user_dic):
    user_path = os.path.join(setting.BASE_DB, '%s.json' % user_dic['name'])
    with open(user_path, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f,ensure_ascii=False)
        f.flush()


def select(name):
    user_path = os.path.join(setting.BASE_DB, '%s.json' % name)
    if os.path.exists(user_path):
        with open(user_path, 'r', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic
    else:
        return None
