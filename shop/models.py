from django.db import models


class Prices(models.Model):
    FUEL = [
        ('АИ-92', 'АИ-92'),
        ('АИ-95', 'АИ-95'),
        ('АИ-98', 'АИ-98'),
        ('ДТ', 'ДТ')
    ]
    shopkey = models.PositiveSmallIntegerField()
    fuel = models.CharField(max_length=64, choices=FUEL)
    price = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    update_date = models.DateTimeField(auto_now_add=True)
    surname = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.shopkey} {self.fuel}: {self.start_date} - {self.end_date}'

class ShopFuel(models.Model):
    shopkey = models.PositiveSmallIntegerField()
    ai92 = models.BooleanField(default=True)
    ai95 = models.BooleanField(default=True)
    ai98 = models.BooleanField(default=True)
    dt = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.shopkey}'