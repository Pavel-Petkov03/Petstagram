# Generated by Django 4.0.2 on 2022-02-06 22:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_petmodel_profilemodel_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 7, 0, 18, 28, 586109)),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 7, 0, 18, 28, 585609)),
        ),
    ]
