# Generated by Django 2.1.4 on 2018-12-26 11:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20181212_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesee',
            name='date_debut',
            field=models.DateField(default=datetime.datetime(2018, 12, 26, 11, 22, 39, 922298, tzinfo=utc)),
        ),
    ]
