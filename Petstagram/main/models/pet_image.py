from django.contrib.postgres.fields import ArrayField
from django.db import models

from Petstagram.main.models import PetModel
from Petstagram.main.validators.image_size_validator import ValidateImage


class PetImage(models.Model):
    NAME_MAX_LENGTH = 30
    MAX_IMAGE_SIZE = 5
    photo = models.ImageField(validators=[
        ValidateImage(MAX_IMAGE_SIZE)
    ])
    tagged_pets = ArrayField(
        models.TextField(models.CharField(max_length=NAME_MAX_LENGTH)
                         ))

    description = models.TextField()

    creation_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    pet_id = models.ForeignKey(PetModel, on_delete=models.CASCADE, default="")

    class Meta:
        db_table = "pet_image"
        app_label = "main"