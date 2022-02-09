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
    first_name = models.CharField(max_length=MAX_FIRST_NAME_LENGTH, validators=[
        NameValidator(MIN_FIRST_NAME_LENGTH, MAX_FIRST_NAME_LENGTH, "first_name"),

    ], blank=False)
    last_name = models.CharField(max_length=MAX_SECOND_NAME_LENGTH, validators=[
        NameValidator(MIN_SECOND_NAME_LENGTH, MAX_SECOND_NAME_LENGTH, "second_name"),
    ], blank=False)
    profile_picture = models.URLField(blank=False)

    # optional

    date_of_birth = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(validators=[
        EmailValidator()
    ], blank=True, null=True)
    gender = models.TextField(choices=GENDER_OPTION, blank=True, null=True)

    class Meta:
        db_table = "profile"
        app_label = "main"
