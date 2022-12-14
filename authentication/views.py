from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from users.models import CustomUser 
from .forms import *

class Sign_in(LoginView):
    form_class = SignInForm
    template_name = 'authentication/signin.html'
    
    
    def get_success_url(self):
        if self.request.user.position.position_name == 'Оператор':
            return reverse('shop:shop')
        else:
            return reverse('authentication:signup')


class Sign_up(CreateView):
    form_class = SignupForm
    template_name = 'authentication/signup.html'
    success_url = reverse_lazy('authentication:signin')

