# -*- coding:utf-8 -*-
# Author:lupengliang


# # 基本使用方法

# ## 获取基本信息
import pyautogui
# 屏幕大小
size = pyautogui.size()
print(size)
# 鼠标位置
mouse_pos = pyautogui.position()
print(mouse_pos)
# 判断点是否在屏幕内
print(pyautogui.onScreen(100,100))


####################################################

import pyautogui
size = pyautogui.size()
# 把鼠标