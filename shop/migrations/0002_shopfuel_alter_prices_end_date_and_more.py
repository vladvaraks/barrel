# Generated by Django 4.0.6 on 2022-08-08 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopFuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopkey', models.PositiveSmallIntegerField()),
                ('ai92', models.BooleanField(default=True)),
                ('ai95', models.BooleanField(default=True)),
                ('ai98', models.BooleanField(default=True)),
                ('dt', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='prices',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='prices',
            name='start_date',
            field=models.DateField(),
        ),
    ]