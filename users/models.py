from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), unique=True, max_length=64)
    surname = models.CharField(_('Фамилия'), max_length=64)
    name = models.CharField(_('name'), max_length=64)
    shopkey = models.SmallIntegerField('Номер АЗС', default=0)
    is_staff = models.BooleanField(_('Персонал'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.username