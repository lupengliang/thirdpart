# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:lupengliang
import platform
from time import sleep

import pyautogui

from basic.base import Base
from basic.data import (data, drive, game_start, PAUSE)


class Logic(Base):
    def __init__(self):
        super().__init__()
        self.pu.FAILSAFE = True
        self.pu.PAUSE = 2.5

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
        self.pu.confirm(text="是否启动炉石传说死鱼骑脚本？", title="提示", buttons=["确定", "取消"])

    # 启动游戏
    def prepare_start(self):
        self.key_board('win', 'r')
        self.key_board('ctrl', 'space')
        self.type('cmd \n')
        self.key_board('ctrl', 'space')
        self.type(f'{drive} \n')
        self.type(f'{data.get("path").get("game_path")} \n')
        self.key_board('alt', 'f4')
        while True:
            try:
                x, y = self.get_picture_center(game_start)
                self.click(x, y)
                sleep(2)
                self.key_board('tab')
                break
            except TypeError:
                pass

    # 冒险对战
    def adventure_begin(self):
        sleep(38)
        self.click(977, 399)  # 点击冒险模式
        self.click(1395, 888)  # 点击选择按钮
        self.click(1395, 888)
        self.click(x=1395, y=108)  # 选择对战对象: 法师
        self.click(1395, 888)  # 点击确定

    # 起手留牌
    def retain_cards(self):
        # 先手留牌
        self.click(x=616, y=494)
        self.click(x=954, y=471)
        self.click(x=1299, y=488)
        self.click(x=964, y=853)  # 点击确定

    # 放牌
    def release_cards(self):
        pyautogui.mouseDown(x=665, y=991, button='left')
        self.absolute_move(952, 492)
        pyautogui.mouseUp()

        # self.click(x=, y=)
        # self.drag()
        # self.click(x=680, y=991)
        # self.drag(x=952, y=492)
        # self.click(x=720, y=991)
        # self.drag(x=952, y=492)
        # self.click(x=760, y=991)
        # self.drag(x=952, y=492)
        # self.click(x=800, y=991)
        # self.drag(x=952, y=492)
        # self.click(x=830, y=991)
        # self.drag(x=952, y=492)
        # self.click(x=860, y=991)
        # self.drag(x=952, y=492)
        # self.click(x=900, y=991)
        # self.drag(x=952, y=492)
        # self.click(x=950, y=991)
        # self.drag(x=952, y=492)
        # self.click(x=960, y=991)
        # self.drag(x=952, y=492)



if __name__ == '__main__':
    lc = Logic()
    lc.prepare_start()
    lc.adventure_begin()
    lc.retain_cards()
    # lc.release_cards()
