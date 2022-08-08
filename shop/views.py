from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.db.models import Max
from datetime import datetime, timedelta, date

from .models import Prices, ShopFuel
from users.models import CustomUser
from .forms import PriceForm, MeasurementForm


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
            date_from_form = datetime.strptime(form.cleaned_data['date'], '%Y-%m-%d') #form.cleaned_data['date']
            id_maxdate_price = Prices.objects.filter(shopkey=user_shopkey[0].shopkey, fuel=form.cleaned_data['fuel'])
            if id_maxdate_price:
                Prices.objects.filter(pk=id_maxdate_price.latest('start_date').id).update(end_date=date_from_form, surname=user_shopkey[0].surname)
                Prices.objects.create(shopkey=user_shopkey[0].shopkey,
                                    fuel=form.cleaned_data['fuel'],
                                    price=form.cleaned_data['price'],
                                    start_date=date_from_form + timedelta(days=1),
                                    end_date=date(2099, 1, 1),
                                    surname=user_shopkey[0].surname)
            return self.form_valid(form)
        else:
            print(form.__dict__)
            print('Не работаем')
            return self.form_invalid(form)


class OthetСhange(FormView):
    form_class = MeasurementForm
    template_name = 'shop/send_othet.html'
    success_url = reverse_lazy('shop:othet_change')

    def get_context_data(self, **kwargs):
        context = super(OthetСhange, self).get_context_data(**kwargs)
        user_shopkey = CustomUser.objects.filter(username=self.request.user)[0].shopkey
        context['input_fuel'] = ShopFuel.objects.filter(shopkey=user_shopkey)[0]
        return context

    #def get(self, request, *args, **kwargs):
    #    user_shopkey = CustomUser.objects.filter(username=request.user)[0].shopkey
    #    
    #    print(user_shopkey)
    #    return super(OthetСhange, self).get(request, *args, **kwargs)

    