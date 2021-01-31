#
# import os
# import random
#
# if __name__ == '__main__':
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "supercrm.settings")
#     import django
#     django.setup()
#     from sales import models
#
#     source_type = (('qq', "qq群"),
#                    ('referral', "内部转介绍"),
#                    ('website', "官方网站"),
#                    ('baidu_ads', "百度推广"),
#                    ('office_direct', "直接上门"),
#                    ('WoM', "口碑"),
#                    ('public_class', "公开课"),
#                    ('website_luffy', "路飞官网"),
#                    ('others', "其它"),)
#     course_choices = (('LinuxL', 'Linux中高级'),
#                ('PythonFullStack', 'Python高级全栈开发'),)
#     obj_list = []
#     for i in range(251):
#
#         d = {
#             'qq': str(1111+i),
#             'name': 'dz技师%s' % i,
#             'source': source_type[random.randint(0, 8)][0],    # 来源
#             'course': course_choices[random.randint(0, 1)][0],    # 咨询课程
#         }
#         obj = models.Customer(**d)
#         obj_list.append(obj)
#     models.Customer.objects.bulk_create(obj_list)

# <!-- 练习其它小知识点 -->
print(divmod(5, 2))  # 商 余

print(chr(90))  # 字母 a-z A-Z

class DataSet(object):
  @property
  def method_with_property(self): ##含有@property
      return 15
  def method_without_property(self): ##不含@property
      return 15

l = DataSet()
print(l.method_with_property) # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）。
print(l.method_without_property())  #没有加@property , 必须使用正常的调用方法的形式，即在后面加()


# <!-- 练习其它小知识点 -->