from django.db import models

# Create your models here.


class UserInfo(models.Model):
    """
    用户表: 销售...
    """
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    email = models.EmailField()
    telephone = models.CharField(max_length=16)
    is_active = models.BooleanField(default=True)