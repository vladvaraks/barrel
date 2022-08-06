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
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    update_date = models.DateTimeField(auto_now_add=True)
    surname = models.CharField(max_length=64)