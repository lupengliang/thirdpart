from django.urls import reverse
from django import template



register = template.Library()


@register.simple_tag
def reverse_url(request):
    if request.path == reverse('customers'):
        return "公户信息"
    else:
        return "我的客户信息"