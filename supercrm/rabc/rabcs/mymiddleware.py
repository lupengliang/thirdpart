import re

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse


class PermissinoAuth(MiddlewareMixin):

    def process_request(self, request):
        request_path = request.path
        # 登录认证白名单
        white_list = [reverse('login'), '/admin/*']
        for i in white_list:
            ret = re.match(i, request.path)
            if ret:
                return

        # 登录认证
        is_login = request.session.get('is_login', None)
        if not is_login:
            return redirect('login')

        # 权限认证白名单
        permission_white_list = [reverse('index')]
        if request_path in permission_white_list:
            return

        # 权限认证
        permission_list = request.session.get('permission_list')


        for reg in permission_list:
                reg = r"^%s$" % reg['permissions_url']
                if re.match(reg, request.path):
                    return
                else:
                    return HttpResponse('你不配!!!')