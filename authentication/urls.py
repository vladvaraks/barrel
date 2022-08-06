from django.contrib import admin
from django.urls import path
from .views import Sign_up, Sign_in
from django.contrib.auth.views import LogoutView

app_name = 'authentication'

urlpatterns = [
    path('signup/', Sign_up.as_view(), name='signup'),
    path('', Sign_in.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), name='signout')
]
