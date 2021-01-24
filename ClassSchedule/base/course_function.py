# -*- coding:utf-8 -*-
# author:lupengliang
import json
import re
import requests
from log.logger import logger


class CourseFunction:
    def __init__(self):
        self.url = 'https://api.bilibili.com/x/player/pagelist?bvid=BV1aJ411H7Ej&jsonp=jsonp'

    # 请求头
    def _heads(self):
        pass

    # 爬取老男孩B站的课程信息
    def draw_courses_content(self, url):
        content = requests.get(url)
        if content.status_code == 200:
            logger.info(f'successful to get information on length is {len(content.text)}.')
            return json.loads(content.text)

    # 处理数据格式 -- 获取课程标题
    def deal_message(self, url):
        json_text = self.draw_courses_content(url)
        multi_data = json_text.get('data')
        for single_data in multi_data:
            print(single_data.get('part'))
        content_list = [[single_data.get('part')] for single_data in multi_data]
        return content_list



if __name__ == '__main__':
    cf = CourseFunction()
    print(cf.deal_message(cf.url))