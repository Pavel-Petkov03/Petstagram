# Generated by Django 4.0.2 on 2022-02-10 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_petimage_creation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petimage',
            name='pet_id',
        ),
        migrations.AlterField(
            model_name='petimage',
            name='creation_date',
            field=models.DateTimeField(),
        ),
        migrations.RemoveField(
            model_name='petimage',
            name='tagged_pets',
        ),
        migrations.AddField(
            model_name='petimage',
            name='tagged_pets',
            field=models.ManyToManyField(to='main.PetModel'),
        ),
    ]
