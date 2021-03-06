from django.http import HttpResponseBadRequest
from django.shortcuts import render

from Petstagram.main.models import ProfileModel


def is_authenticated_decorator(func):
    def main(*args, **kwargs):
        if check_if_has_profile():
            return func(*args, **kwargs)
        return HttpResponseBadRequest("not authenticated")

    return main


def check_if_has_profile():
    return ProfileModel.objects.exists()


def error_page(req, exception=None):
    return render(req, "401_error.html")


@is_authenticated_decorator
def view(req):
    return render(req, "home_page.html")
