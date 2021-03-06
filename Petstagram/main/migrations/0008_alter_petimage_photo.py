# Generated by Django 4.0.2 on 2022-02-08 20:25

import Petstagram.main.validators.image_size_validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_petimage_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petimage',
            name='photo',
            field=models.ImageField(upload_to='', validators=[Petstagram.main.validators.image_size_validator.ValidateImage(5)]),
        ),
    ]
