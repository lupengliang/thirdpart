# -*- coding:utf-8 -*-
# author: lupengliang
from logger.logging_setting import logger

# 操作excel的基层方法
class excel:
    def __init__(self):
        pass

    # 向一个excel中写入一行数据
    def add_row_data(self):
        pass

    # 向一个excel中写入一列数据
    def add_col_data(self):
        pass

    # 向一个excel的单元格写入数据
    def add_cell_data(self):
        pass

    # 将两个excel中的行数补齐
    def full_rows(self):
        pass

    # 将两个excel中的列数补齐
    def full_cols(self):
        pass

if __name__ == '__main__':
    ex = excel()
    logger.info('hello world')
