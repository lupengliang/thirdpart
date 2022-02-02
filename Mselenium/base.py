# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lupengliang
from time import sleep, time

from PIL import Image
from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class WebOperation:
    # 实例化对象
    @classmethod
    def get_waiter(cls, browser):
        waiter = WebDriverWait(browser, 60)
        return waiter

    # 定位: 获取元素
    def get_element(self, browser, ele_tuple):
        waiter = self.get_waiter(browser)
        element = waiter.until(ec.presence_of_element_located(ele_tuple))
        return element

    # 鼠标: 左击
    def left_click(self, browser, ele_tuple):
        element = self.get_element(browser, ele_tuple)
        element.click()

    # 鼠标: 右击
    def right_click(self, browser, ele_tuple):
        element = self.get_element(browser, ele_tuple)
        element.context_click().perform()

    # 鼠标: 双击
    def double_click(self, browser, ele_tuple):
        element = self.get_element(browser, ele_tuple)
        element.double_click().perform()

    # 鼠标: 悬停
    def hover(self, browser, ele_tuple):
        element = self.get_element(browser, ele_tuple)
        ActionChains(browser).move_to_element(element).perform()

    # 文本: 获取当前的url
    @classmethod
    def get_url(cls, browser):
        return browser.current_url

    # 文本: 获取当前页面的源码
    @classmethod
    def get_source(cls, browser):
        return browser.page_source

    # 文本: 输入文本
    def input_text(self, browser, ele_tuple, value):
        ele = self.get_element(browser, ele_tuple)
        ele.clear()
        ele.send_keys(value)

    # 文本: 获取元素上的文本
    def get_text(self, browser, ele_tuple):
        ele = self.get_element(browser, ele_tuple)
        return ele.text

    # 断言: 获取网页的标题是否为某个值
    def get_title(self, browser, text):
        waiter = self.get_waiter(browser)
        result = waiter.until(ec.title_is(text))
        return result

    # 断言: 某段文本是否在某个元素上
    def verify_text(self, browser, ele_tuple, text):
        waiter = self.get_waiter(browser)
        result = waiter.until(ec.text_to_be_present_in_element(ele_tuple, text))
        return result

    # 键盘: 模拟键盘按键ctrl + '*'
    def press_key(self, browser, ele_tuple, key: str):
        ele = self.get_element(browser, ele_tuple)
        ele.send_keys(Keys.CONTROL, key)

    # 滚动条: 下拉
    @classmethod
    def scroll_pull(cls, browser):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    # 滚动条: 上拉 >> ??
    @classmethod
    def scroll_push(cls, browser):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    # 滚动条: 翻屏
    @classmethod
    def scroll_screen(cls, browser):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(1)

    # 下拉框: 文本
    @classmethod
    def select_by_string(cls, browser, text):
        Select(browser).select_by_visible_text(text)
        sleep(1)

    # 下拉框: 索引
    @classmethod
    def select_by_index(cls, browser, option_index):
        Select(browser).select_by_index(option_index)
        sleep(1)

    # 下拉框: 值value
    @classmethod
    def select_by_value(cls, browser, value):
        Select(browser).select_by_value(value)
        sleep(1)

    # 下拉框: 选择第一个选项
    @classmethod
    def select_by_first(cls, browser):
        Select(browser).first_selected_option()
        sleep(1)

    # 框架: 当框架可以切入时，立刻切入
    def switch_frame(self, browser, frame_tuple):
        waiter = self.get_waiter(browser)
        waiter.until(ec.frame_to_be_available_and_switch_to_it(frame_tuple))

    # 句柄: 获取当前所有的句柄
    @classmethod
    def get_handles(cls, browser):
        handles = browser.window_handles
        return handles

    # 句柄: 获取当前网页的句柄,切换到指定窗口
    @classmethod
    def switch_handles(cls, browser, window_index):
        handles = cls.get_handles(browser)
        browser.switch_to.window(handles[window_index])

    # 窗口: 警告窗口点击确定
    @classmethod
    def click_accept(cls, browser):
        alerter = browser.switch_to.alert
        alerter.accept()

    # 窗口: 警告窗口点击取消
    @classmethod
    def click_dismiss(cls, browser):
        alerter = browser.switch_to.alert
        alerter.dismiss()

    # 窗口: 警告窗口获取文本
    @classmethod
    def get_alarm_text(cls, browser):
        alerter = browser.switch_to.alert
        return alerter.text

    # 属性: 获取元素上的某个属性的值
    def get_attribute_value(self, browser, ele_tuple, attribute_name):
        ele = self.get_element(browser, ele_tuple)
        attribute_value = ele.get_attribute(attribute_name)
        return attribute_value

    # 属性: 去除某个元素的某个属性
    def remove_attribute(self, browser, ele_tuple, attribute_name):
        js = 'arguments[0].removeAttribute("%s")' % attribute_name
        ele = self.get_element(browser, ele_tuple)
        browser.execute_script(js, ele)
        return ele

    # 属性: 去除元素的只读属性
    def remove_readonly_from_element_and_send_keys(self, browser, ele_tuple, attributeName, value):
        """
        ele = self.remove_attribute(browser, ele_tuple, "readonly")
        ele.clear()
        ele.send_keys(value)
        """
        ele = self.remove_attribute(browser, ele_tuple, "readonly")
        # 封装设置页面对象的属性值的方法
        # 调用JavaScript代码修改页面元素的属性值进行替换，并执行该JavaScript代码
        browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])", self.get_element(browser, ele_tuple), attributeName, value)
        return ele

    # 图片: 截图保存图片
    @staticmethod
    def get_picture(browser, picture_path):
        picture_format = picture_path + "/" + time() + ".png"
        sleep(2)
        browser.get_screenshop_as_file(picture_format)

    # 图片: 保存大图 裁剪图片 获取验证码图片
    def crop_picture(self, browser, ele_tuple, local_image, image_name):  # .png格式
        screen_shot = browser.get_screenshop_as_file(local_image)
        code_img_tag = self.get_element(browser, ele_tuple)
        location = code_img_tag.location  # 验证码左下角的x,y坐标
        size = code_img_tag.size  # 验证码的长宽
        # 裁剪的验证码区域范围
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))
        i = Image.open(screen_shot)  # 保存验证码
        frame = i.crop(rangle)  # 开始裁剪
        frame.save(image_name)


if __name__ == '__main__':
    options = ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(r'chromedriver.exe', options=options)
    driver.get('http://www.baidu.com')
