from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


from .managers import CustomUserManager

class PositionNames(models.Model):
    position_name = models.CharField('Должность', unique=True, max_length=64)

    def __str__(self):
        return self.position_name


class Departments(models.Model):
    DEPARTAMENT = [
        ('0', 'Нет подразделения'),
        ('1', 'Кемерово'),
        ('2', 'Белово'),
        ('3', 'Межгород'),
    ]
    internal_code = models.SmallIntegerField('Внутренний код', default=0, unique=True)
    division = models.CharField('Подразделение', default=0, choices=DEPARTAMENT, max_length=10)
    shopkey = models.SmallIntegerField('Номер для отображения', default=0, unique=True)
    shopkey_oc = models.SmallIntegerField('Номер в ОЦ', default=0, unique=True)
    name = models.CharField('Наименование', max_length=128)

    def __str__(self):
        
        return f'{self.get_division_display()} - {self.name}'

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), unique=True, max_length=64)
    surname = models.CharField(_('Фамилия'), max_length=64)
    name = models.CharField(_('name'), max_length=64)
    shopkey = models.ForeignKey('Departments', to_field='internal_code', default=0, on_delete=models.PROTECT)
    position = models.ForeignKey('PositionNames', max_length=64, default=1, on_delete=models.PROTECT)
    is_staff = models.BooleanField(_('Персонал'), default=False)
    is_active = models.BooleanField(_('active'), default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.username
