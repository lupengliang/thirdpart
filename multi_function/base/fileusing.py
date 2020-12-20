# -*- coding: utf-8 -*-
# author: lupengliang

from logger.logging_setting import logger

# class of handling file
class FileClass():
    def __init__(self):
        pass

    # write data to file
    def write_data(self,filepath, content):
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            logger.info(f'successful to write message to {filepath.split("/")[-1]} file.')

    # read data to file
    def read_data(self, filepath):
        with open(filepath, encoding='utf-8') as f:
            content = f.read()
            logger.info(f'successful to read data from {filepath.split("/")[-1]} file.')
            return content

if __name__ == '__main__':
    fc = FileClass()
    info = "hello world"
    fc.write_data('./cclean.txt', info)
    print(fc.read_data('./cclean.txt'))

