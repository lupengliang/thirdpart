from django.urls import reverse
from django import template
from django.http.request import QueryDict


register = template.Library()


@register.simple_tag
def reverse_url(request):
    print(type(request.GET))
    if request.path == reverse('customers'):
        return "公户信息"
    else:
        return "我的客户信息"


# 跳转到原路径自定义标签
@register.simple_tag
def resole_url(request, url_name, customer_pk):
    # 编辑保存之后跳转回的路径
    next_url = request.get_full_path()
    reverse_url = reverse(url_name, args=(customer_pk,))
    q = QueryDict(mutable=True)
    q['next'] = next_url
    next_url = q.urlencode()
    full_url = reverse_url + '?' + next_url
    return full_url