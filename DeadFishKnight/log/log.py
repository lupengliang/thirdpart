# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:lupengliang
import logging


class Logger(object):
    level_relations = {  # 日志级别关系映射
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self, filename, level='info', fmt='%(asctime)s [%(filename)s][line:%(lineno)d]: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(self.level_relations.get(level))
        self.logger.handlers.clear()
        sh = logging.StreamHandler()
        sh.setFormatter(format_str)
        self.logger.addHandler(sh)


logger_obj = Logger('execute.log', level='debug')
logger = logger_obj.logger


if __name__ == '__main__':
    logger_obj = Logger('execute.log', level='debug')
    logger = logger_obj.logger
    logger.info('hello world')
