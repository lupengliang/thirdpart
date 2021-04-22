from django.conf import settings
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import (
    render, redirect
)
from django.db import transaction
from django.urls import reverse
from django.views import View

from sales import models
from sales.utils.page import MyPagenation
from sales.myforms import (
    CustomerForm, ConsultRecordForm, EnrollForm
)
# Create your views here


# 首页
def home(request):
    return render(request, 'saleshtml/home.html')


# 公户私户信息展示
class CutomerView(View):
    def get(self, request):
        current_request_path = request.path
        # 公户
        if current_request_path == reverse('customers'):
            tag = '1'
            customer_list = models.Customer.objects.filter(consultant_id__isnull=True)
        else:
            # 私户请求,查询所有的私户
            tag = '2'
            user_obj = request.user_obj
            customer_list = models.Customer.objects.filter(consultant=user_obj)
        # 分页和搜索
        get_data = request.GET.copy()  # 将request.GET对象变为可修改的
        page_num = request.GET.get('page')  # 当前页 例如 1
        search_field = request.GET.get('search_field')  # 选择查询的字段
        kw = request.GET.get('kw')  # 查询关键字
        if kw:
            kw = kw.strip()
            q_obj = Q()
            q_obj.children.append((search_field, kw))
            customer_list = customer_list.filter(q_obj)
        else:
            customer_list = customer_list
        base_url = request.path
        customer_count = customer_list.count()
        per_page_num = settings.PER_PAGE_NUM
        page_num_show = settings.PAGE_NUM_SHOW
        page_obj = MyPagenation(page_num, customer_count, base_url, get_data, per_page_num, page_num_show)
        page_html = page_obj.page_html()
        customer_objs = customer_list.reverse()[page_obj.start_data_num: page_obj.end_data_num]
        return render(request, 'saleshtml/customers.html', {'customer_objs': customer_objs, 'page_html': page_html, 'tag': tag})

    def post(self, request):
        action = request.POST.get('action')
        cids = request.POST.getlist('cids')
        if hasattr(self, action):
            print(cids)
            ret = getattr(self, action)(request, cids)
            if ret:
                return ret
            return redirect(request.path)

    # 公转私
    def reverse_gs(self, request, cids):
        # 事务select语句加锁
        with transaction.atomic():
            customers = models.Customer.objects.filter(pk__in=cids, consultant__isnull=True)
        if customers.count() != len(cids):
            return HttpResponse('回家练手速吧!')
        customers.update(consultant_id=request.session.get('user_id'))

    # 私转公
    def reverse_sg(self, request, cids):
        customers = models.Customer.objects.filter(pk__in=cids, consultant=request.user_obj)
        customers.update(consultant=None)


# 添加客户和编辑客户
def add_edit_customer(request, cid=None):
    """
    添加客户和编辑客户
    :param rquest:
    :param cid:  客户记录id
    :return:
    """
    label = '编辑客户' if cid else '添加客户'
    customer_obj = models.Customer.objects.filter(pk=cid).first()
    if request.method == 'GET':
        customer_form = CustomerForm(instance=customer_obj)
        return render(request, 'saleshtml/edit_customer.html',
                      {'customer_form': customer_form,
                       'label': label})
    else:
        next_url = request.GET.get('next')
        customer_form = CustomerForm(request.POST, instance=customer_obj)
        if customer_form.is_valid():
            customer_form.save()
            return redirect(next_url)
        else:
            return render(request, 'saleshtml/edit_customer.html', {'customer_form': customer_form, 'label': label})


# 跟进记录管理
class ConsultRecordView(View):

    def get(self, request):
        # 当前用户的未删除的客户跟进记录
        cid = request.GET.get('cid')
        # 如果存在cid,那么找的是单个客户的跟进记录
        if cid:
            consult_list = models.ConsultRecord.objects.filter(consultant=request.user_obj,
                                                               delete_status=False, customer_id=cid).order_by('-date')
        else:
            consult_list = models.ConsultRecord.objects.filter(consultant=request.user_obj,
                                                delete_status=False).order_by('-date')
        # 分页和搜索
        get_data = request.GET.copy()  # 将request.GET对象变为可修改的
        page_num = request.GET.get('page')  # 当前页 例如 1
        search_field = request.GET.get('search_field')  # 选择查询的字段
        kw = request.GET.get('kw')  # 查询关键字
        if kw:
            kw = kw.strip()
            q_obj = Q()
            q_obj.children.append((search_field, kw))
            consult_list = consult_list.filter(q_obj)
        else:
            consult_list = consult_list
        base_url = request.path
        consult_count = consult_list.count()
        per_page_num = settings.PER_PAGE_NUM
        page_num_show = settings.PAGE_NUM_SHOW
        page_obj = MyPagenation(page_num, consult_count, base_url, get_data, per_page_num, page_num_show)
        page_html = page_obj.page_html()
        consult_objs = consult_list.reverse()[page_obj.start_data_num: page_obj.end_data_num]
        return render(request, 'saleshtml/consultrecord.html',
                      {'consult_list': consult_objs, 'page_html': page_html})

    def post(self, request):
        action = request.POST.get('action')
        cids = request.POST.getlist('cids')
        if hasattr(self, action):
            consults = models.Customer.objects.filter(pk__in=cids)
            getattr(self, action)(request, consults)
            return redirect(request.path)

    # 公转私
    def bulk_delete(self, request, consults):
        consults.update(delete_status=True)


class AddEditConsultView(View):

    def get(self, request, cid=None):
        """
        添加客户和编辑客户
        :param rquest:
        :param cid:  客户记录id
        :return:
        """
        if cid:
            pass
        label = '编辑跟进记录' if cid else '添加跟进记录'
        consult_obj = models.ConsultRecord.objects.filter(pk=cid).first()
        if request.method == 'GET':
            consult_form = ConsultRecordForm(request, instance=consult_obj)
            return render(request, 'saleshtml/add_edit_consult.html',
                          {'consult_form': consult_form,
                           'label': label})

    def post(self, request, cid=None):
        consult_obj = models.ConsultRecord.objects.filter(pk=cid).first()
        next_url = request.GET.get('next')
        if not next_url:
            next_url = reverse('consult_record')
        consult_form = ConsultRecordForm(request, request.POST, instance=consult_obj)
        if consult_form.is_valid():
            consult_form.save()
            return redirect(next_url)
        else:
            return render(request, 'saleshtml/edit_customer.html', {'consult_form': consult_form})


# 报名表信息展示
class EnrollmentView(View):
    def get(self, request):
        enrolls = models.Enrollment.objects.filter(
            customer__consultant=request.user_obj, delete_status=False)

        return render(request, 'saleshtml/enrollments.html', {'enrolls': enrolls})

    def post(self, request):
        pass


# 添加跟进记录
class AddEditEnrollView(View):

    def get(self, request, cid=None):
        """
        添加客户和编辑客户
        :param rquest:
        :param cid:  客户记录id
        :return:
        """
        label = '编辑报名信息' if cid else '添加报名信息'
        enroll_obj = models.ConsultRecord.objects.filter(pk=cid).first()
        if request.method == 'GET':
            enroll_form = EnrollForm(request, instance=enroll_obj)
            return render(request, 'saleshtml/add_edit_enroll.html',
                          {'enroll_form': enroll_form,
                           'label': label})

    def post(self, request, cid=None):
        enroll_obj = models.Enrollment.objects.filter(pk=cid).first()
        next_url = request.GET.get('next')
        if not next_url:
            next_url = reverse('consult_record')
        enroll_form = EnrollForm(request, request.POST, instance=enroll_obj)
        if enroll_form.is_valid():
            enroll_form.save()
            return redirect(next_url)
        else:
            return render(request, 'saleshtml/edit_customer.html', {'enroll_form': enroll_form})





# 课程记录表
class CourseRecordView(View):

    def get(self, request):
        course_records = models.CourseRecord.objects.all()

        return render(request, 'saleshtml/courserecord.html', {'course_records': course_records})

    def post(self, request):
        action = request.POST.get('action')
        cids = request.POST.getlist('cids')

        if hasattr(self, action):
            getattr(self, action)(request, cids)
        return HttpResponse('ok')

    # 批量生成学习记录
    def bulk_create_srecord(self, request, cids):
        for cid in cids:
            course_record_obj = models.CourseRecord.objects.filter(pk=cid).first()
            students = course_record_obj.re_class.customer_set.filter(status='studying')
            obj_list = []
            for student in students:
                obj = models.StudyRecord(
                    course_record_id=cid,
                    student=student,
                )
                obj_list.append(obj)
            models.StudyRecord.objects.bulk_create(obj_list)

from django.forms.models import modelformset_factory
from django import forms
class StudyRecordModelForm(forms.ModelForm):


    class Meta:
        model = models.StudyRecord
        fields = "__all__"

class StudyRecordView(View):

    def get(self, request, course_record_id):
        print(course_record_id)
        # queryset = models.StudyRecord.objects.filter(
        #     course_record_id=course_record_id
        # )
        formset_cls = modelformset_factory(model=models.StudyRecord, form=StudyRecordModelForm, extra=0)
        study_records = models.StudyRecord.objects.filter(
            course_record_id=course_record_id
        )
        formset = formset_cls(queryset=study_records)

        return render(request, 'saleshtml/studyrecord.html', {'formset': formset})

    def post(self, request, course_record_id):
        formset_cls = modelformset_factory(model=models.StudyRecord,
                                           form=StudyRecordModelForm, extra=0)
        formset = formset_cls(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect(request.path)
        else:
            return render(request, 'saleshtml/studyrecord.html', {'formset': formset})
