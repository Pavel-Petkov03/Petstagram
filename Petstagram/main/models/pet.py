from django.db import models

from Petstagram.main.models import ProfileModel


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
    date = models.DateTimeField(blank=True, null=True)
    user_profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = "pet"
        app_label = "main"
