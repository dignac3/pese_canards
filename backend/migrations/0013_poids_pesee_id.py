# Generated by Django 2.1.7 on 2019-02-17 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_auto_20190213_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='poids',
            name='pesee_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
