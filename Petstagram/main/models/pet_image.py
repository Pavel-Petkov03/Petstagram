from django.db import models

from Petstagram.main.validators.image_size_validator import ValidateImage
from Petstagram.main.models.pet import PetModel


class PetImage(models.Model):
    photo = models.FileField(validators=[
        ValidateImage(5)
    ])

    tagged_pets = models.TextField(
        choices=PetModel.objects.all()  # will change this when stackoverflow is available
    )
