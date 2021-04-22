from django.conf.urls import url
from django.contrib import admin
from sales.views import (
    auth, customer
)

urlpatterns = [
    url(r'^login/', auth.login, name='login'),    # 登录
    url(r'^register/', auth.register, name='register'),    # 注册
    url(r'^home/', customer.home, name='home'),    # 首页
    # 所有客户信息展示
    url(r'^customers', customer.CutomerView.as_view(), name='customers'),
    # 我的客户
    url(r'^mycustomers', customer.CutomerView.as_view(), name='mycustomers'),
    # 添加页面
    # url(r'^add_customer', views.add_customer, name='add_customer'),
    url(r'^add_customer', customer.add_edit_customer, name='add_customer'),
    # 编辑客户
    # url(r'^edit_customer/(\d+)/', views.edit_customer, name='edit_customer'),
    url(r'^edit_customer/(\d+)/', customer.add_edit_customer, name='edit_customer'),

    # 跟进记录展示
    url(r'^consult_record', customer.ConsultRecordView.as_view(), name='consult_record'),

    # 添加跟进记录
    url(r'^add_consult_record', customer.AddEditConsultView.as_view(), name='add_consult_record'),

    # 编辑跟进记录
    url(r'^edit_consult_record/(\d+)/', customer.AddEditConsultView.as_view(), name='edit_consult_record'),

    # 报名表信息展示
    url(r'^enrollment/', customer.EnrollmentView.as_view(), name='enrollment'),

    # 添加报名信息
    url(r'^enroll_add/', customer.AddEditEnrollView.as_view(), name='enroll_add'),

    # 编辑报名信息
    url(r'^enroll_edit/(\d+)/', customer.AddEditEnrollView.as_view(), name='enroll_edit'),

    # 课程记录
    url(r'^course_record/', customer.CourseRecordView.as_view(), name='course_record'),

    # 查看学习记录
    url(r'^study_record/(\d+)/', customer.StudyRecordView.as_view(), name='study_record'),
]