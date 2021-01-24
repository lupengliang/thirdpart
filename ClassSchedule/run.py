# -*- coding:utf-8 -*-
# author:lupengliang
from base.course_function import CourseFunction
from base.excel_operation import ExcelOperation


class CoreFunction:
    def __init__(self):
        self.cf = CourseFunction()
        self.eo = ExcelOperation()

    # 开始运行
    def run(self, excel_name):
        content = self.cf.deal_message(self.cf.url)
        self.eo.create_excel(excel_name=excel_name)
        self.eo.load_excel(excel_name=excel_name, data=content)


if __name__ == '__main__':
    cf = CoreFunction()
    cf.run(excel_name='course.xlsx')
