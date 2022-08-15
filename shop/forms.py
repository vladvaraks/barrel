from django import forms
from django.contrib.admin import widgets
from datetime import timedelta

from .models import *
from users.models import CustomUser
from office.models import ShopFuel


class DateInput(forms.DateInput):
    input_type = 'date'

class PriceForm(forms.ModelForm):
    date = forms.CharField(widget=DateInput(), label='Дата окончания')
    price = forms.FloatField(label='Новая цена')

    class Meta:
        model = Prices
        fields = ('fuel', )
        labels = {'fuel':'Топливо'}

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PriceForm, self).__init__(*args, **kwargs)
        self.fields['fuel'].empty_label = 'Выберите топливо'

    def clean(self):
        allowed_fuel = ShopFuel.objects.filter(shopkey=self.request.user.shopkey).values()[0]
        if not allowed_fuel[self.cleaned_data['fuel'].slug_name]:
            raise forms.ValidationError('На данной АЗС не разрешен данный вид топлива, обратитесь в поддержку.')
            

    
class SendingMoneyForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.input_money = kwargs.pop('input_money', None)
        del self.input_money['id'], self.input_money['shopkey_id']
        labels = {
            'sdano': 'Cдано', 
            'fuel_cards': 'Топливные карты', 
            'sber': 'Сбер', 
            'benzuber': 'BENZUBER', 
            'petrol': 'Петрол+', 
            'e100': 'E-100', 
            'fuelup': 'FuelUP', 
            'vedomost': 'Ведомость', 
            'lnr': 'ЛНР', 
            'skidka': 'Скидка', 
            'rashod': 'Расход'
        }
        super(SendingMoneyForm, self).__init__(*args, **kwargs)
        for money, value in self.input_money.items():
            if value == True:
                self.fields[f'{money}'] = forms.IntegerField()
                self.fields[f'{money}'].label = labels[money]
                self.fields[f'{money}'].widget.attrs['class'] = 'form-control text-center'
                self.fields[f'{money}'].widget.attrs['placeholder'] = 'Введите значение'


class SendingVolumeForm(forms.Form):        

    def __init__(self, *args, **kwargs):
        self.input_fuel = kwargs.pop('input_fuel', None)
        self.date_othet = kwargs.pop('date_othet', None)
        self.request = kwargs.pop('request', None)
        super(SendingVolumeForm, self).__init__(*args, **kwargs)
        for fuel, value in self.input_fuel.items():
            if value == True:
                self.fields[f'measurement_{fuel}'] = forms.IntegerField()
                self.fields[f'counter_{fuel}'] = forms.IntegerField()
                self.fields[f'strait_{fuel}'] = forms.IntegerField()
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control text-center'
            visible.field.widget.attrs['placeholder'] = 'Введите значение'

    def clean(self):
        print('SendingVolumeForm')
        #raise forms.ValidationError('Логин должен быть больше 8 букв')
    #    yesterday_othet = FuelSelling.objects.filter(shopkey = self.request.user.shopkey,
    #                                date_othet = self.date_othet - timedelta(days=1)
    #                                )
    #    print(yesterday_othet)   
