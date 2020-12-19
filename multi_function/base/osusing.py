# -*- coding:utf-8 -*-
# author: lupengliang
import os

from logger.logging_setting import logger
import shutil


class OSClass():
    def __init__(self):
        pass

    # 获取当前路径下的所有文件
    def get_all_file(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        all_file = os.listdir(current_path)
        logger.info(f'successful to get all the file as this {all_file}.')
        return all_file

    # 拼接文件名与路径
    def concat_path(self, filepath, filename):
        absulte_path = os.path.join(filepath, filename)
        return absulte_path

    # 移动当前文件到指定目录
    def move_file(self, filepath, target_path):
        shutil.move(filepath, target_path)
        logger.info(f'successful to move file {filepath.split("/")[-1]} to {target_path}.')

    # 删除指定目录下的文件
    def delete_file(self, filepath):
        os.remove(filepath)
        logger.info(f'successful to delete {filepath.split("/")[-1]} file.')

    # 对指定目录下的文件进行重命名
    def rename_file(self, filename, filepath, targetpath):
        if filename not in targetpath:
            os.rename(filepath, targetpath)
        else:
            logger.error(f'this {targetpath} has a same file, so has overwrited.')
        logger.info(f'successful to rename file.')

if __name__ == '__main__':
    oc = OSClass()
    oc.delete_file('./cclean.txt')