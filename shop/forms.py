from django import forms
from django.contrib.admin import widgets 

from .models import Prices


class DateInput(forms.DateInput):
    input_type = 'date'

class PriceForm(forms.Form):
    FUEL = [
        ('АИ-92', 'АИ-92'),
        ('АИ-95', 'АИ-95'),
        ('АИ-98', 'АИ-98'),
        ('ДТ', 'ДТ')
    ]
    date = forms.CharField(widget=DateInput(), label='Дата окончания')
    fuel = forms.ChoiceField(choices=FUEL, label='Топливо')
    price = forms.FloatField(label='Новая цена')

    #def clean(self):
    #    #print(self.__dict__)
    #    raise forms.ValidationError('Логин должен быть больше 8 букв')