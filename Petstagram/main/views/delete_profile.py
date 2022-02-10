from django.shortcuts import render, redirect
from django.views import View

from Petstagram.main.models import ProfileModel, PetImage, PetModel
from Petstagram.main.views.error_page import is_authenticated_decorator


class DeleteProfileView(View):
    @is_authenticated_decorator
    def get(self, req):
        return render(req, "profile_delete.html")

    @is_authenticated_decorator
    def post(self, req):
        ProfileModel.objects.all().delete()
        PetImage.objects.all().delete()
        PetModel.objects.all().delete()
        return redirect("/")
