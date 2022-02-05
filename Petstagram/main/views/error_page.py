from django.shortcuts import render


def is_authenticated(func):
    def main(*args, **kwargs):
        # will add profile logic
        return func(*args, **kwargs)
    return main


def error_page(req):
    return render(req, "401_error.html")
