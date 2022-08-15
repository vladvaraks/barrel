from urllib import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.db.models import Max
from datetime import datetime, timedelta, date
from django.views.generic.edit import FormMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .multiforms import MultiFormsView
from office.models import *
from .models import *
from users.models import CustomUser
from .forms import *


class SelectShop(TemplateView):
    template_name = 'shop/selectshop.html'

class SelectOthet(TemplateView):
    template_name = 'shop/selectothet.html'
    

class PriceСhange(FormView):
    form_class = PriceForm
    template_name = 'shop/pricechange.html'
    success_url = reverse_lazy('shop:price_change')

    def get_form_kwargs(self):
        kwargs = super(PriceСhange, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            date_from_form = datetime.strptime(form.cleaned_data['date'], '%Y-%m-%d') #form.cleaned_data['date']
            id_maxdate_price = Prices.objects.filter(shopkey=self.request.user.shopkey.internal_code, fuel=form.cleaned_data['fuel'])
            if id_maxdate_price:
                Prices.objects.filter(pk=id_maxdate_price.latest('start_date').id).update(end_date=date_from_form, surname=self.request.user.surname)
                Prices.objects.create(shopkey=self.request.user.shopkey,
                                    fuel=form.cleaned_data['fuel'],
                                    price=form.cleaned_data['price'],
                                    start_date=date_from_form + timedelta(days=1),
                                    end_date=date(2099, 1, 1),
                                    surname=self.request.user.surname)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class OthetСhange(MultiFormsView):
    form_classes = { 'SendingVolume': SendingVolumeForm,
                     'SendingMoney': SendingMoneyForm}
    template_name = 'shop/send_othet.html'
    success_url = reverse_lazy('shop:othet_change')


    def get_form_kwargs(self, form_name):
        kwargs = super(OthetСhange, self).get_form_kwargs(form_name)
        if form_name == 'SendingVolume':
            kwargs['input_fuel'] = ShopFuel.objects.filter(shopkey=self.request.user.shopkey).values('ai92','ai95','ai98','dt')[0]
            kwargs['date_othet'] = FuelSelling.objects.filter(shopkey=self.request.user.shopkey).aggregate(Max('date_othet'))['date_othet__max']  + timedelta(days=1)
            kwargs['request'] = self.request
        else:
            kwargs['input_money'] = ShopMoney.objects.filter(shopkey=self.request.user.shopkey)\
                .values()[0]
            #kwargs['request'] = self.request
        return kwargs

    #def get_context_data(self, **kwargs):
    #    context = super(OthetСhange, self).get_context_data(**kwargs)
    #    return context

    def post(self, request, *args, **kwargs):
        forms = self.get_forms()
        date_othet = forms['SendingVolume'].date_othet
        if forms['SendingVolume'].is_valid() and forms['SendingMoney'].is_valid():
            add_entry = []
            for fuel, value in forms['SendingVolume'].input_fuel.items():
                if value == True:
                    add_entry.append(FuelSelling(shopkey=self.request.user.shopkey,
                            date_othet = date_othet,
                            fuel = fuel,
                            volume_measurements = forms['SendingVolume'].cleaned_data[f'measurement_{fuel}'],
                            counter = forms['SendingVolume'].cleaned_data[f'counter_{fuel}'],
                            strait = forms['SendingVolume'].cleaned_data[f'strait_{fuel}'],
                            surname = self.request.user.surname))
            FuelSelling.objects.bulk_create(add_entry)
            return self.forms_valid(forms)
        else: 
            return self.forms_invalid(forms)




#class OthetСhange(FormView):
#    form_class = SendingVolumeForm
#    template_name = 'shop/send_othet.html'
#    success_url = reverse_lazy('shop:othet_change')
#
#    def get_form_kwargs(self):
#        kwargs = super(OthetСhange, self).get_form_kwargs()
#        kwargs['input_fuel'] = ShopFuel.objects.filter(shopkey=self.request.user.shopkey).values('ai92','ai95','ai98','dt')[0]
#        kwargs['date_othet'] = FuelSelling.objects.filter(shopkey=self.request.user.shopkey).aggregate(Max('date_othet'))['date_othet__max'] + timedelta(days=1)
#        kwargs['request'] = self.request
#        return kwargs
#
#    def get_context_data(self, **kwargs):
#        context = super(OthetСhange, self).get_context_data(**kwargs)
#        return context
#
#    def post(self, request, *args, **kwargs):
#        form = self.get_form()
#        date_othet = form.date_othet
#        if form.is_valid():
#            add_entry = []
#            for fuel, value in form.input_fuel.items():
#                if value == True:
#                    add_entry.append(FuelSelling(shopkey=self.request.user.shopkey,
#                            date_othet = date_othet,
#                            fuel = fuel,
#                            volume_measurements = form.cleaned_data[f'measurement_{fuel}'],
#                            counter = form.cleaned_data[f'counter_{fuel}'],
#                            strait = form.cleaned_data[f'strait_{fuel}'],
#                            surname = self.request.user.surname))
#            FuelSelling.objects.bulk_create(add_entry)
#            return self.form_valid(form)
#        else: 
#            return self.form_invalid(form)


    #def get_context_data(self, **kwargs):
    #    context = super(OthetСhange, self).get_context_data(**kwargs)
    #    print(context['form'].input_fuel)
    #    #context['input_fuel'] = self.get_form_kwargs().get('input_fuel')
    #    print('get_context_data')
    #    return context


#class OthetСhange(FormView):
#    form_class = SendingVolumeForm
#    template_name = 'shop/send_othet.html'
#    success_url = reverse_lazy('shop:othet_change')
#
#    def get_form_kwargs(self):
#        kwargs = super(OthetСhange, self).get_form_kwargs()
#        print('get_form_kwargs')
#        user_shopkey = CustomUser.objects.filter(username=self.request.user)[0].shopkey
#        kwargs['input_fuel'] = ShopFuel.objects.filter(shopkey=user_shopkey).values('ai92','ai95','ai98','dt')[0]
#        return kwargs
#
#    def get_context_data(self, **kwargs):
#        context = super(OthetСhange, self).get_context_data(**kwargs)
#        print('get_context_data')
#        #user_shopkey = CustomUser.objects.filter(username=self.request.user)[0].shopkey
#        #context['date_othet'] = Measurements.objects.filter(shopkey=user_shopkey).aggregate(Max('date_othet'))['date_othet__max'] + timedelta(days=1)
#        #context['input_fuel'] = ShopFuel.objects.filter(shopkey=user_shopkey)[0]
#        context['input_fuel'] = self.get_form_kwargs().get('input_fuel')
#        return context
#
#    def post(self, request, *args, **kwargs):
#        form = self.get_form()
#        user_shopkey = self.get_context_data().get('input_fuel').shopkey
#        date_othet = self.get_context_data().get('date_othet')
#        #print(date_othet)
#        if form.is_valid() and (date.today() > date_othet):
#            Counters.objects.create(shopkey=user_shopkey,
#                                    date_othet=date_othet,
#                                    counter_ai92=form.cleaned_data['counter_ai92'],
#                                    counter_ai95=form.cleaned_data['counter_ai95'],
#                                    counter_ai98=form.cleaned_data['counter_ai98'],
#                                    counter_dt=form.cleaned_data['counter_dt'],
#                                    surname=request.user)
#            Measurements.objects.create(shopkey=user_shopkey,
#                                        date_othet=date_othet,
#                                        volume_ai92=form.cleaned_data['measurement_ai92'],
#                                        volume_ai95=form.cleaned_data['measurement_ai95'],
#                                        volume_ai98=form.cleaned_data['measurement_ai98'],
#                                        volume_dt=form.cleaned_data['measurement_dt'],
#                                        surname=request.user)
#            return self.form_valid(form)
#        else:
#            
#            return self.form_invalid(form)
#
#    #def get(self, request, *args, **kwargs):
#    #    user_shopkey = CustomUser.objects.filter(username=request.user)[0].shopkey
#    #    
#    #    print(user_shopkey)
#    #    return super(OthetСhange, self).get(request, *args, **kwargs)


