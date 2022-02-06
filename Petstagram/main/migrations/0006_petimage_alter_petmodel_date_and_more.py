# Generated by Django 4.0.2 on 2022-02-06 22:46

import Petstagram.main.validators.image_size_validator
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_petmodel_date_alter_profilemodel_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='', validators=[Petstagram.main.validators.image_size_validator.ValidateImage(5)])),
                ('tagged_pets', models.TextField(choices=[])),
            ],
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 7, 0, 46, 5, 719018)),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 7, 0, 46, 5, 718025)),
        ),
    ]