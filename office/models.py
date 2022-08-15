from django.db import models

class Fuel(models.Model):
    name = models.CharField(max_length=64)
    slug_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'


class PaymentType(models.Model):
    name = models.CharField(max_length=64)
    slug_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'


class ShopFuel(models.Model):
    shopkey = models.ForeignKey('users.Departments', to_field='internal_code', on_delete=models.PROTECT)
    ai92 = models.BooleanField(default=True)
    ai95 = models.BooleanField(default=True)
    ai98 = models.BooleanField(default=True)
    dt = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.shopkey}'


class ShopMoney(models.Model):
    shopkey = models.ForeignKey('users.Departments', to_field='internal_code', on_delete=models.PROTECT)
    sdano = models.BooleanField(default=True)
    fuel_cards = models.BooleanField(default=True)
    sber = models.BooleanField(default=True)
    benzuber = models.BooleanField(default=True)
    petrol = models.BooleanField(default=True)
    e100 = models.BooleanField(default=True)
    fuelup = models.BooleanField(default=True)
    vedomost = models.BooleanField(default=True)
    lnr = models.BooleanField(default=True)
    skidka = models.BooleanField(default=True)
    rashod = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.shopkey}'
