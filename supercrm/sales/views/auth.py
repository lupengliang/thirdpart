from django.shortcuts import (
    render, redirect
)

from sales import models
from sales.utils.hashlib_func import set_md5
from sales.myforms import RegisterForm

# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.UserInfo.objects.filter(username=username, password=set_md5(password)).first()
        if user_obj:
            # 将用户信息保存到session中
            request.session['user_id'] = user_obj.id
            return redirect('customers')
        else:
            return render(request, 'login.html', {'error': '用户名或者密码错误'})


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