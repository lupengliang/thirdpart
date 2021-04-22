# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:lupengliang
import os
import re

import yaml


def get_position(content: str):
    return re.findall("(\d+)", content)


class GetData:
    def __init__(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        self.config_path = os.path.join(os.path.dirname(current_path), 'config/config.yaml')

    # 读取参数文件
    def get_data(self):
        with open(self.config_path, encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    # 获取盘符
    @classmethod
    def get_drive(cls, path):
        return path[:2]


data = GetData().get_data()
# 启动结构
drive = GetData.get_drive(path=data.get('path').get('game_path'))
cmd_picture = data.get('path').get('win_path')
game_start = data.get('path').get('start_game')

# 配置信息
PAUSE = data.get('settings').get('PAUSE')

# 游戏模式
adventure_model = data.get('path').get('adventure_model')

# 游戏难度
practice_model = data.get('path').get('practice_model')  # 练习模式
normal_model = data.get('path').get('normal_model')  # 普通难度


# 通用按钮
start_button = data.get('position').get('common')  # 开始按钮/选择按钮

if __name__ == '__main__':
    print(get_position('Point(x=610, y=431)'))
    print(normal_model)
    print(data)
