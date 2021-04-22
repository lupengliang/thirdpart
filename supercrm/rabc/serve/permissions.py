
from django.conf import settings

def init_permission(request, user_obj):
    request.session['is_login'] = True  # 用来记录是否登录

    # 登录成功,将权限信息注入到session中
    permission_list = user_obj.roles.values(
        'permissions_url',
        'permissions_title',
        'permissions_is_menu',
        'permissions_icon'
    ).distinct()

    menu_list = []  # 菜单栏权限 [{},]
    for permission in permission_list:
        is_menu = permission.get('permissions_is_menu')
        if is_menu:
            menu_list.append(permission)
    print('menu_list>>>', menu_list)

    # 注入认证权限url
    request.session[settings.PERMISSION_KEY] = list(permission_list)

    # 注入菜单展示的url
    request.session[settings.MENU_KEY] = menu_list

    print('permission_list', permission_list)