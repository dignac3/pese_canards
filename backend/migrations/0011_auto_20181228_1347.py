# Generated by Django 2.1.4 on 2018-12-28 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20181228_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poids',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 28, 13, 47, 35, 121218)),
        ),
    ]