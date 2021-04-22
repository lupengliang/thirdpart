import re

from django import forms
from django.core.exceptions import ValidationError


from sales import models


# 手机号格式验证
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')  # 自定义验证规则的时候，如果不符合你的规则，需要自己发起错误


# 注册功能相关验证
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
                                                  'oncontextmenu': 'return false', 'onpaste': 'return false', }),
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


# 添加客户和编辑客户
class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = '__all__'

    error_messages = {
        'qq': {'required': '不能为空'},
        'course': {'required': '不能为空'},
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from multiselectfield.forms.fields import MultiSelectFormField
        from django.forms.fields import DateField
        for field_name, field in self.fields.items():
            print(type(field))
            if not isinstance(field, MultiSelectFormField):
                field.widget.attrs.update({'class': 'form-control'})
            if isinstance(field, DateField):
                field.widget.attrs.update({'type': 'date'})


# 添加跟进和编辑跟进
class ConsultRecordForm(forms.ModelForm):

    class Meta:
        model = models.ConsultRecord
        fields = '__all__'
        exclude = ['delete_status']
    # sex = forms.ChoiceField(
    #     choices=(('1', '男'), ('2', '女'))
    # )

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            if field_name == 'customer':
                field.queryset = models.Customer.objects.filter(
                    consultant=request.user_obj)
            elif field_name == 'consultant':
                field.queryset = models.UserInfo.objects.filter(pk=request.user_obj.pk)
                # field.choices = ((request.user_obj.pk, request.user_obj.username),)


# 添加和编辑报名信息
class EnrollForm(forms.ModelForm):

    class Meta:
        model = models.Enrollment
        fields = '__all__'

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            if field_name == 'customer':
                field.queryset = models.Customer.objects.filter(
                    consultant=request.user_obj)
            elif field_name == 'consultant':
                field.queryset = models.UserInfo.objects.filter(pk=request.user_obj.pk)
                # field.choices = ((request.user_obj.pk, request.user