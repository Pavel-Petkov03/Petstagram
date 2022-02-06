from datetime import datetime

from django.core.validators import EmailValidator
from django.db import models

from Petstagram.main.validators.name_validator import NameValidator


class ProfileModel(models.Model):
    # constants
    MAX_FIRST_NAME_LENGTH = 30
    MAX_SECOND_NAME_LENGTH = 30
    MIN_FIRST_NAME_LENGTH = 2
    MIN_SECOND_NAME_LENGTH = 2

    GENDER_OPTION = (
        ("Male", "MALE"),
        ("Female", "Female"),
        ("Do not show", "Do not show"),
    )

    # required
    first_name = models.CharField(max_length=30, validators=[
        NameValidator(MIN_FIRST_NAME_LENGTH, MAX_FIRST_NAME_LENGTH, "first_name"),

    ], blank=False)
    last_name = models.CharField(max_length=30, validators=[
        NameValidator(MIN_SECOND_NAME_LENGTH, MAX_SECOND_NAME_LENGTH, "second_name"),
    ], blank=False)
    profile_picture = models.URLField(blank=None)

    # optional

    date_of_birth = models.DateTimeField(default=datetime.now())
    description = models.TextField(default="")
    email = models.EmailField(validators=[
        EmailValidator()
    ], default="")
    gender = models.TextField(choices=GENDER_OPTION, default="")

    class Meta:
        db_table = "profile"
        app_label = "main"
