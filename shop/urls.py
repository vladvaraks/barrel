from django.contrib import admin
from django.urls import path

from .views import SelectShop, SelectOthet, PriceСhange, OthetСhange

app_name = 'shop'

urlpatterns = [
    path('', SelectShop.as_view(), name='shop'),
    path('selectothet/', SelectOthet.as_view(), name='shop_select_othet'),
    path('selectothet/price', PriceСhange.as_view(), name='price_change'),
    path('selectothet/othet', OthetСhange.as_view(), name='othet_change'),
]
