from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.db.models import Max
import datetime

from .models import Prices
from users.models import CustomUser
from .forms import PriceForm


class SelectShop(TemplateView):
    template_name = 'shop/selectshop.html'

class SelectOthet(TemplateView):
    template_name = 'shop/selectothet.html'
    

class PriceСhange(FormView):
    form_class = PriceForm
    template_name = 'shop/pricechange.html'
    success_url = reverse_lazy('shop:price_change')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user_shopkey = CustomUser.objects.filter(username=request.user)
            print(form.cleaned_data['fuel'])
            print('Работаем')
            #print(Prices.objects.filter(shopkey=user_shopkey).values('shopkey', 'id').annotate(Max('start_date')))
            id_maxdate_price = Prices.objects.filter(shopkey=user_shopkey[0].shopkey, fuel=form.cleaned_data['fuel'])
            if id_maxdate_price:
                Prices.objects.filter(pk=id_maxdate_price.latest('start_date').id).update(end_date=form.cleaned_data['date'], surname=user_shopkey[0].surname)
                Prices.objects.create(shopkey=user_shopkey[0].shopkey,
                                    fuel=form.cleaned_data['fuel'],
                                    price=form.cleaned_data['price'],
                                    start_date=form.cleaned_data['date'],
                                    end_date=form.cleaned_data['date'],
                                    surname=user_shopkey[0].surname)
            return self.form_valid(form)
        else:
            print(form.__dict__)
            print('Не работаем')
            return self.form_invalid(form)
