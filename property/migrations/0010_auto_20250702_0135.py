# Generated by Django 2.2.24 on 2025-07-01 22:35

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_fill_owner_pure_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owners_phonenumber',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер владельца'),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Номер владельца')),
                ('pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='RU', verbose_name='Нормализованный номер')),
                ('flats', models.ManyToManyField(blank=True, related_name='owners', to='property.Flat', verbose_name='Квартиры')),
            ],
        ),
    ]
