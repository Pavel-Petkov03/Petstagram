from django.db import models

from Petstagram.main.validators.name_validator import NameValidator


class ProfileModel(models.Model):
    MAX_FIRST_NAME_LENGTH = 30
    MAX_SECOND_NAME_LENGTH = 30
    MIN_FIRST_NAME_LENGTH = 2
    MIN_SECOND_NAME_LENGTH = 2

    first_name = models.CharField(max_length=30, validators=[
        NameValidator(MIN_FIRST_NAME_LENGTH, MAX_FIRST_NAME_LENGTH, "first_name"),
    ])
    last_name = models.CharField(max_length=30, validators=[
        NameValidator(MIN_SECOND_NAME_LENGTH, MAX_SECOND_NAME_LENGTH, "second_name"),
    ])
    profile_picture = models.URLField()

    class Meta:
        db_table = "profile"
        app_label = "main"
