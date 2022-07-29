from django import forms
from django.contrib.auth import authenticate, password_validation
from django.contrib.auth.forms import UserCreationForm, \
    AuthenticationForm


from users.models import CustomUser


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'surname', 'name', 'position', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Введите логин',
            }),
            'surname': forms.TextInput(attrs={
                'placeholder': 'Введите фамилию',
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Введите имя',
            })
        }

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        #if len(username) < 8:
        #    raise forms.ValidationError('Логин должен быть больше 8 букв')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        
        print(password1)
        print(password2)

        if not password2:
            raise forms.ValidationError('Поле не может быть пустым!')

        if password1 != password2:
            raise forms.ValidationError('Пароли должны совпадать!')

        return password2

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Пароль'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Подтверждение пароля'
        })


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }))        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def clean(self):
        username = self.cleaned_data.get('username').lower()
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(
                self.request,
                username=username,
                password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.error_messages['inactive'] = 'Для активации аккаунта обратитесь в службу поддержки.'
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

