# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:lupengliang
from logic.logic import Logic


class Main(Logic):
    def __init__(self):
        super().__init__()

    # 启动游戏
    def run(self):
        self.start_game()
        self.prepare_start()


if __name__ == '__main__':
    main = Main()
    main.run()
