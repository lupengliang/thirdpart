# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:lupengliang
import os

import yaml


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
drive = GetData.get_drive(path=data.get('path').get('game_path'))
print(drive)
