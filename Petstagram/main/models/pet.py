from datetime import datetime

from django.db import models


class PetModel(models.Model):
    # constants
    NAME_MAX_LENGTH = 30
    CHOICES = (
        ("DOG", "Dog"),
        ("Cat", "Cat"),
        ("Bunny", "Bunny"),
        ("Parrot", "Parrot"),
        ("Fish", "Fish"),
        ("Other", "Other"),
    )

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    type = models.TextField(choices=CHOICES, default="")

    description = models.TextField(default="")
    date = models.DateTimeField(default=datetime.now())
    likes = models.IntegerField()

    class Meta:
        db_table = "pet"
        app_label = "main"
