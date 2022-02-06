from django.shortcuts import render

from Petstagram.main.models import ProfileModel


def is_authenticated_middleware(func):
    def main(*args, **kwargs):
        # will add profile logic
        return func(*args, **kwargs)
    return main


def check_if_has_profile():
    return ProfileModel.objects.exists()


def error_page(req, exception=None):
    return render(req, "401_error.html")
