# -*- coding:utf-8 -*-
# author: lupengliang
import os

from logger.logging_setting import logger
import shutil

# class of move | rename | copy | delete
class OSClass():
    def __init__(self):
        pass

    # get all file names of current path
    def get_all_file(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        all_file = os.listdir(current_path)
        logger.info(f'successful to get all the file as this {all_file}.')
        return all_file

    # join point filepath and filename
    def concat_path(self, filepath, filename):
        absulte_path = os.path.join(filepath, filename)
        return absulte_path

    # move file of current path to point path
    def move_file(self, filepath, target_path):
        shutil.move(filepath, target_path)
        logger.info(f'successful to move file {filepath.split("/")[-1]} to {target_path}.')

    # delete file of point path
    def delete_file(self, filepath):
        os.remove(filepath)
        logger.info(f'successful to delete {filepath.split("/")[-1]} file.')

    # rename file of point path
    def rename_file(self, filename, filepath, targetpath):
        if filename not in targetpath:
            os.rename(filepath, targetpath)
        else:
            logger.error(f'this {targetpath} has a same file, so has overwrited.')
        logger.info(f'successful to rename file.')

if __name__ == '__main__':
    oc = OSClass()
    oc.delete_file('./cclean.txt')