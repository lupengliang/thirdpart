# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:lupengliang
from base.data import PAUSE
from logic.logic import Logic


class Main(Logic):
    def __init__(self):
        super().__init__()
        self.pu.FAILSAFE = True
        self.pu.PAUSE = PAUSE

    # 启动游戏
    def run(self):
        self.start_game()
        self.prepare_start()
        self.adventure_begin()


if __name__ == '__main__':
    main = Main()
    main.run()
