from django.shortcuts import render, redirect
from django.views import View

from Petstagram.main.forms.pet_create import PetCreateForm
from Petstagram.main.models import PetModel
from Petstagram.main.views.error_page import is_authenticated_decorator


class EditPetView(View):
    @is_authenticated_decorator
    def get(self, req, pk):
        form = PetCreateForm(instance=PetModel.objects.get(id=pk))
        return render(req, "pet_edit.html", {
            "form": form
        })

    @is_authenticated_decorator
    def post(self, req, pk):
        form = PetCreateForm(req.POST, instance=PetModel.objects.get(id=pk))
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(req, "pet_edit.html", {
            "form": form
        })
