# Generated by Django 2.1.7 on 2019-02-13 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20181228_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesee',
            name='date_debut',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pesee',
            name='fichier',
            field=models.FileField(upload_to='files/'),
        ),
    ]