# Generated by Django 4.0.2 on 2022-02-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_petmodel_date_alter_petmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petmodel',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
