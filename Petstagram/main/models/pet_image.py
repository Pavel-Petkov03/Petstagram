from django.contrib.postgres.fields import ArrayField
from django.db import models

from Petstagram.main.validators.image_size_validator import ValidateImage


class PetImage(models.Model):
    NAME_MAX_LENGTH = 30
    photo = models.FileField(validators=[
        ValidateImage(5)
    ])
    tagged_pets = ArrayField(
        models.TextField(models.CharField(max_length=NAME_MAX_LENGTH)
                         ))

    description = models.TextField()

    creation_date = models.DateTimeField()
    likes = models.IntegerField()
