# Generated by Django 5.1.2 on 2024-10-28 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0002_hotel_address_en_hotel_address_ru_hotel_city_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=16, null=True),
        ),
    ]