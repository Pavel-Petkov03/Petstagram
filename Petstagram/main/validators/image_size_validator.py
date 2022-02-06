from django.core.exceptions import ValidationError

class ValidateImage():
    def __init__(self, file):
        self.file = file

    def __call__(self, max_size):
        filesize = self.file.size
        if filesize > max_size * 1024 ** 2:  # this is in megabytes
            raise ValidationError("The file size must be max 5 mb")
