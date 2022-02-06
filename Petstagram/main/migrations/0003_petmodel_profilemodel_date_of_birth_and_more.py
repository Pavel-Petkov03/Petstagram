# Generated by Django 4.0.2 on 2022-02-06 22:18

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_profilemodel_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('type', models.TextField(choices=[('DOG', 'Dog'), ('Cat', 'Cat'), ('Bunny', 'Bunny'), ('Parrot', 'Parrot'), ('Fish', 'Fish'), ('Other', 'Other')], default='')),
                ('description', models.TextField(default='')),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 2, 7, 0, 18, 20, 880579))),
                ('likes', models.IntegerField()),
            ],
            options={
                'db_table': 'pet',
            },
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 7, 0, 18, 20, 879576)),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='email',
            field=models.EmailField(default='', max_length=254, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='gender',
            field=models.TextField(choices=[('Male', 'MALE'), ('Female', 'Female'), ('Do not show', 'Do not show')], default=''),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='profile_picture',
            field=models.URLField(blank=None),
        ),
    ]
