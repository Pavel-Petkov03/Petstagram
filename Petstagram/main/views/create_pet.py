from django.shortcuts import render, redirect
from django.views import View

from Petstagram.main.forms.pet_create import PetCreateForm
from Petstagram.main.models import ProfileModel, PetModel
from Petstagram.main.views.error_page import is_authenticated_decorator


class CreatePetView(View):
    @is_authenticated_decorator
    def get(self, req):
        return render(req, "pet_create.html", {
            "form": PetCreateForm()
        })

    @is_authenticated_decorator
    def post(self, req):
        form = PetCreateForm(req.POST, instance=PetModel(user_profile=ProfileModel.objects.first()))
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(req, "pet_create.html", {
            "form": form
        })
