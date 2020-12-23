# -*- coding:utf-8 -*-
# author: lupengliang


import logging
import os
from logging import handlers

# custom logging formatter
class Logger(object):
    level_relations = {  # relation of logging map
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename, level='info', when='D', backCount=3,
                 fmt='%(asctime)s [%(filename)s][line:%(lineno)d]: %(message)s'):
       self.logger = logging.getLogger(filename)
       format_str = logging.Formatter(fmt)  # setting log formatter
       self.logger.setLevel((self.level_relations.get(level)))  # setting log level
       self.logger.handlers.clear()  # first clear handle
       sh = logging.StreamHandler()  # setting output in cmd
       sh.setFormatter(format_str)  # setting logging formatter of you want to this
       th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount, encoding='utf-8')
       th.setFormatter(format_str)  # setting formatter of writing file
       self.logger.addHandler(sh)  # add object to to logger
       self.logger.addHandler(th)
       # self.logger.removeHandler(sh)  # second remove handle

logger_obj = Logger('execute.log', level='debug')
logger = logger_obj.logger

if __name__ == '__main__':
    logger_obj = Logger('execute.log', level='debug')
    logger = logger_obj.logger
    logger.info('hello world')