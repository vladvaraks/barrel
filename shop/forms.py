from django import forms
from django.contrib.admin import widgets 

from .models import Prices, ShopFuel
from users.models import CustomUser


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

    #def __init__(self, *args, **kwargs):
    #    self.request = kwargs.pop("request")
    #    self.user_shopkey = CustomUser.objects.filter(username=self.request.user)
    #    global create_form
    #    create_form = ShopFuel.objects.filter(shopkey=self.user_shopkey)
    #    super(MeasurementForm, self).__init__(*args, **kwargs)

class MeasurementForm(forms.Form):

    ai92 = forms.IntegerField(required = False)
    ai95 = forms.IntegerField(required = False)
    ai98 = forms.IntegerField(required = False)
    dt = forms.IntegerField(required = False)



