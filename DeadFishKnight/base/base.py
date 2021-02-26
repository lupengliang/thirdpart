# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:lupengliang
import pyautogui


class Base:
    def __init__(self):
        self.pu = pyautogui
        self.pu.FAILSAFE = True
        self.pu.PAUSE = 2.5

    # 获取当前的位置
    def get_position(self, x, y):
        return self.pu.position(x, y)

    # 获取屏幕的尺寸大小
    def get_size(self):
        return self.pu.size()

    # 检查坐标是否在屏幕上
    def position_exist(self, x, y):
        return self.pu.onScreen(x, y)

    # 绝对移动
    def absolute_move(self, x, y, duration):
        return self.pu.moveTo(x, y, duration)

    # 相对移动
    def relative_move(self, xOffset, yOffset, duration):
        return self.pu.moveRel(xOffset, yOffset, duration)

    # 键盘按键组合 － 启动游戏
    def key_board(self, *args, **kwargs):
        self.pu.hotkey(*args, **kwargs)

    # 移动
    def move(self, xOffset, yOffset):
        return self.pu.move(xOffset, yOffset)

    # 单击
    def click(self, x, y, clicks=1):
        self.pu.click(x, y, clicks)

    # 双击
    def double_click(self, x, y):
        self.pu.doubleClick(x, y)

    # 右键点击
    def right_click(self, x, y):
        self.pu.rightClick(x, y)

    # 加载图片
    def load_picture(self):
        pass

    # 发现战吼牌
    def find_card(self):
        pass

    # 简单输入文本
    def type(self, message):
        self.pu.typewrite(message)

    # 鼠标拖拽
    def drag(self, x, y, duration=1, button='left'):
        self.pu.dragTo(x, y, duration, button)

    # 定位图片中心位置
    def get_picture_center(self, *args, **kwargs):
        self.pu.locateCenterOnScreen(*args, **kwargs)

    # 定位局部图片返回坐标
    def get_picture_position(self, *args, **kwargs):
        return list(self.pu.locateAllOnScreen(*args, **kwargs))

    # 生成alert
    def alert(self, text: str, title: str, button: str, timeout=800):
        return self.pu.alert(text, title, button, timeout)

    # 生成确认窗口
    def confirm(self, text: str, title: str, buttons: list):
        self.pu.confirm(text, title, buttons)


if __name__ == '__main__':
    be = Base()
    # be.key_board('win', 'd')

