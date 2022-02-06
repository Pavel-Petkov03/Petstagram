from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NameValidator:
    def __init__(self, min_length, max_length, name_of_field):
        self.min_length = min_length
        self.max_length = max_length
        self.name_of_filed = name_of_field

    def __call__(self, value):
        if self.check_max_length(value) or self.check_min_length(value) or self.check_if_only_letters_exist(value):
            raise ValidationError(
                f"The {self.name_of_filed} must be max {self.max_length} and min {self.min_length} and consist only letters")

    def check_min_length(self, value):
        return value.__len__ < self.min_length

    def check_max_length(self, value):
        return value.__len__ > self.max_length

    @staticmethod
    def check_if_only_letters_exist(value):
        for char in value:
            if not char.isalpha():
                return True
        return False
