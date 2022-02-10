from django.db import models

from Petstagram.main.models import PetModel
from Petstagram.main.validators.image_size_validator import ValidateImage


class PetImage(models.Model):
    NAME_MAX_LENGTH = 30
    MAX_IMAGE_SIZE = 5
    photo = models.ImageField(validators=[
        ValidateImage(MAX_IMAGE_SIZE)
    ])
    tagged_pets = models.ManyToManyField(PetModel)

    description = models.TextField()

    creation_date = models.DateTimeField()
    likes = models.IntegerField()

    class Meta:
        db_table = "pet_image"
        app_label = "main"
