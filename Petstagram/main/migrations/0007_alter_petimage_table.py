# Generated by Django 4.0.2 on 2022-02-08 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_petmodel_date_alter_profilemodel_date_of_birth'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='petimage',
            table='pet_image',
        ),
    ]