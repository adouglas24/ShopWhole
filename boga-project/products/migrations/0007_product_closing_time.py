# Generated by Django 3.0.7 on 2020-07-11 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200711_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='closing_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 11, 11, 42, 35, 8861)),
        ),
    ]
