# Generated by Django 3.1.7 on 2021-02-27 23:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_auto_20210213_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupaciente',
            name='vence',
            field=models.DateField(default=datetime.datetime(2021, 3, 29, 23, 25, 34, 348452)),
        ),
    ]
