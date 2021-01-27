import re
import hashlib

from django.shortcuts import (
    render, HttpResponse, redirect
)
from django.core.exceptions import ValidationError
from django import forms

from sales import models
from sales.utils.hashlib_func import set_md5

# Create your views here.


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.UserInfo.objects.filter(username=username, password=set_md5(password)).first()
        if user_obj:
            return redirect('customers')
        else:
            # return redirect('login')
            return render(request, 'login.html', {'error': '用户名或者密码错误'})


def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')  # 自定义验证规则的时候，如果不符合你的规则，需要自己发起错误


# 注册功能
class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        min_length=6,
        label='用户名',
        widget=forms.widgets.TextInput(attrs={'class': 'username', 'placeholder': '输入用户名', 'autocomplete': 'off'}),
        error_messages={
            'required': '用户名不能为空',
            'max_length': '用户名不能大于16位',
            'min_length': '用户名不能小于6位',
        },
    )
    password = forms.CharField(
        max_length=32,
        min_length=6,
        label='密码',
        widget=forms.widgets.PasswordInput(attrs={'class': 'password', 'placeholder': '输入密码',
                                                  'oncontextmenu': 'return false', 'onpaste': 'return false',}),
        error_messages={
            'required': '密码不能为空',
            'max_length': '密码不能大于32位',
            'min_length': '密码不能小于6位',
        }
    )
    r_password = forms.CharField(
        label='确认密码',
        widget=forms.widgets.PasswordInput(attrs={'class': 'password', 'placeholder': '请再次输入密码',
                                                  'oncontextmenu': 'return false', 'onpaste': 'return false', }),
        error_messages={
            'required': '确认密码不能为空',
        }
    )
    telephone = forms.CharField(
        label='手机号',
        widget=forms.widgets.TextInput(attrs={'class': 'phone_number', 'placeholder': '输入手机号码',
                                              'autocomplete': 'off', 'id': 'number'}),
        error_messages={
          'required': '手机号不能为空',
        },
        validators=[mobile_validate, ]
    )
    email = forms.EmailField(
        label='邮箱',
        widget=forms.widgets.TextInput(attrs={'class': 'email', 'placeholder': '输入邮箱地址',
                                                  'oncontextmenu': 'return false', 'type': 'email'}),
        error_messages={
            'required': '邮箱不能为空',
            'invalid': '邮箱格式不对',
        }
        # validators=[]
    )

    # 全局钩子: 校验密码与确认密码是否一致
    def clean(self):
        values = self.cleaned_data
        password = values.get('password')
        r_password = values.get('r_password')
        if password == r_password:
            return values
        else:
            self.add_error('r_password', '再次输入的密码不一致!')


# 注册功能
def register(request):
    """
    注册功能
    :param request:
    :return:
    """
    # 基于form的数据校验
    if request.method == 'GET':
        register_form_obj = RegisterForm()
        return render(request, 'register.html', {'register_form_obj': register_form_obj})
    else:
        register_form_obj = RegisterForm(request.POST)
        if register_form_obj.is_valid():
            print(register_form_obj.cleaned_data)
            register_form_obj.cleaned_data.pop('r_password')
            password = register_form_obj.cleaned_data.pop('password')

            # 对密码进行加密
            password = set_md5(password)
            register_form_obj.cleaned_data.update({'password': password})
            models.UserInfo.objects.create(
                **register_form_obj.cleaned_data
            )
            return redirect('login')
        else:
            return render(request, 'register.html', {'register_form_obj': register_form_obj})


def home(request):
    return render(request, 'saleshtml/home.html')


def customers(request):
    # 当前页 例如 1
    page_num = request.GET.get('page')

    per_page_num = 10    # 每页显示10条
    '''
        1       0               10
        2       10              20
        3       20              30
        ..      (page-1)*10     page*10
    '''
    customer_objs = models.Customer.objects.all()[(int(page_num)-1)*per_page_num: int(page_num)*per_page_num]
    return render(request, 'saleshtml/customers.html', {'customer_objs': customer_objs})