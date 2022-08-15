from django.db import models

class Prices(models.Model):
    shopkey = models.ForeignKey('users.Departments', to_field='internal_code', on_delete=models.PROTECT)
    fuel = models.ForeignKey('office.Fuel', on_delete=models.PROTECT)
    price = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    update_date = models.DateTimeField(auto_now_add=True)
    surname = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.shopkey} {self.fuel}: {self.start_date} - {self.end_date}'

class FuelSelling(models.Model):
    shopkey = models.ForeignKey('users.Departments', to_field='internal_code', on_delete=models.PROTECT)
    fuel = models.ForeignKey('office.Fuel', on_delete=models.PROTECT)
    date_othet = models.DateField()
    volume_measurements = models.PositiveIntegerField()
    counter = models.PositiveIntegerField()
    strait = models.PositiveIntegerField()
    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    surname = models.CharField(max_length=64)


class MoneySelling(models.Model):
    shopkey = models.ForeignKey('users.Departments', to_field='internal_code', on_delete=models.PROTECT)
    payment_type = models.ForeignKey('office.PaymentType', on_delete=models.PROTECT)
    date_othet = models.DateField()
    amount = models.PositiveIntegerField()
    date_add = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    surname = models.CharField(max_length=64)

