from django.contrib import admin
from django.urls import path
from .views import Sign_up, Sign_in

app_name = 'authentication'

urlpatterns = [
    path('signup/', Sign_up.as_view(), name='signup'),
    path('signin/', Sign_in.as_view(), name='signin'),
]
