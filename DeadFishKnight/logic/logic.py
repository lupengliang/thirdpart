# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:lupengliang
import platform

from base.base import Base
from base.data import (data, drive)


class Logic(Base):
    def __init__(self):
        super().__init__()

    # 结束回合
    def job_done(self):
        pass

    # 打脸
    def beat_face(self):
        pass

    # 奇数解场
    def odd_solve(self):
        pass

    # 偶数解场
    def even_solve(self):
        pass

    # 释放法术
    def release_magic(self):
        pass

    # 发送表情
    def send_face(self):
        pass

    # 随机时间
    def random_time(self):
        pass

    # 屏蔽敌人表情
    def shield_face(self):
        pass

    # 提示是否开启
    def start_game(self):
        system = platform.system()
        if system == 'windows':
            self.pu.alert(text="支持windows运行", title="提示", button="确定", timeout=800)
        else:
            self.pu.alert(text="程序只支持windows", title="提示", button="确定")
        confirm = self.pu.confirm(text="是否启动炉石传说死鱼骑脚本？", title="提示", buttons=["确定", "取消"])

    # 启动游戏
    def prepare_start(self):
        self.key_board('win', 'r')
        self.key_board('ctrl', 'space')
        self.type('cmd \n')
        self.key_board('ctrl', 'space')
        self.type(f'{drive} \n')
        self.type(f'{data.get("path").get("game_path")} \n')


if __name__ == '__main__':
    pass
