# -*- coding:utf-8 -*-
# author: lupengliang


import logging
import os
from logging import handlers

# 定置打印日志
class Logger(object):
    level_relations = {  # 日志级别关系映射
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename, level='info', when='D', backCount=3,
                 fmt='%(asctime)s [%(filename)s][line:%(lineno)d]: %(message)s'):
       self.logger = logging.getLogger(filename)
       format_str = logging.Formatter(fmt)  # 设置日志格式
       self.logger.setLevel((self.level_relations.get(level)))  # 设置日志级别
       self.logger.handlers.clear()  # 每次被调用后，清空已经存在handler
       sh = logging.StreamHandler()  # 往屏幕上输出
       sh.setFormatter(format_str)  # 设置日志显示的格式
       th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount, encoding='utf-8')
       th.setFormatter(format_str)  # 设置文件里写入的格式
       self.logger.addHandler(sh)  # 把对象加到logger里
       self.logger.addHandler(th)
       # self.logger.removeHandler(sh)  # 再次移除handles  根据实际情况进行取消注释

logger_obj = Logger('execute.log', level='debug')
logger = logger_obj.logger

if __name__ == '__main__':
    logger_obj = Logger('execute.log', level='debug')
    logger = logger_obj.logger
    logger.info('hello world')