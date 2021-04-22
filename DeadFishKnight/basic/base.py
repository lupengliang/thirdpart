# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:lupengliang
import time

import pyautogui

from basic.data import PAUSE
from log.log import logger


class Base:
    def __init__(self):
        self.pu = pyautogui
        self.screen_width, self.screen_height = self.pu.size()
        self.pu.FAILSAFE = True
        self.pu.PAUSE = PAUSE

    # 获取当前的位置
    def get_position(self, x=None, y=None):
        logger.info(f'position: {self.pu.position(x, y)}')
        return self.pu.position(x, y)

    # 获取屏幕的尺寸大小
    def get_size(self):
        logger.info(f'screen size: {self.pu.size()}')
        return self.pu.size()

    # 检查坐标是否在屏幕上
    def position_exist(self, x, y):
        logger.info(f'position exist: {self.pu.onScreen(x, y)}')
        return self.pu.onScreen(x, y)

    # 绝对移动
    def absolute_move(self, x, y, duration=2):
        logger.info(f'absolute move: {self.pu.moveTo(x, y, duration)}')
        return self.pu.moveTo(x, y, duration)

    # 相对移动
    def relative_move(self, xOffset, yOffset, duration):
        logger.info(f'relative move: {self.pu.moveRel(xOffset, yOffset, duration)}')
        return self.pu.moveRel(xOffset, yOffset, duration)

    # 键盘按键组合 － 启动游戏
    def key_board(self, *args, **kwargs):
        self.pu.hotkey(*args, **kwargs)

    # 移动
    def move(self, xOffset, yOffset):
        logger.info(f'common move: {self.pu.move(xOffset, yOffset)}')
        return self.pu.move(xOffset, yOffset)

    # 单击
    def click(self, x, y, clicks=1, duration=1):
        logger.info(f'click: {self.pu.click(x, y, clicks)}')
        return self.pu.click(x, y, clicks, duration)

    # 双击
    def double_click(self, x, y):
        logger.info(f'click: {self.pu.doubleClick(x, y)}')
        self.pu.doubleClick(x, y)

    # 右键点击
    def right_click(self, x, y):
        logger.info(f'right click: {self.pu.rightClick(x, y)}')
        self.pu.rightClick(x, y)

    # 加载图片
    def load_picture(self):
        pass

    # 发现战吼牌
    def find_card(self):
        pass

    # 简单输入文本
    def type(self, message):
        logger.info(f'message: {message}')
        self.pu.typewrite(message)

    # 鼠标拖拽
    def drag(self, x, y, duration=2, button='left'):
        self.pu.dragTo(x, y, duration, button)

    # 定位图片中心位置
    def get_picture_center(self, *args, **kwargs):
        logger.info(f'picture: {self.pu.locateCenterOnScreen(*args, **kwargs)}')
        return self.pu.locateCenterOnScreen(*args, **kwargs)

    # 定位局部图片返回坐标
    def get_picture_position(self, *args, **kwargs):
        logger.info(f'partial position: {list(self.pu.locateAllOnScreen(*args, **kwargs))}')
        return list(self.pu.locateAllOnScreen(*args, **kwargs))

    # 生成alert
    def alert(self, text: str, title: str, button: str, timeout=800):
        return self.pu.alert(text, title, button, timeout)

    # 生成确认窗口
    def confirm(self, text: str, title: str, buttons: list):
        self.pu.confirm(text, title, buttons)

    # 放牌
    def release(self, x, y):
        self.pu.mouseDown(x, y)
        self.pu.moveTo(x=self.screen_width/2, y=self.screen_height/2)
        self.pu.mouseUp(x=self.screen_width/2, y=self.screen_height/2)


if __name__ == '__main__':
    be = Base()
    while True:
        time.sleep(3)
        be.get_position()