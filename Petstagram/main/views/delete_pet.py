from django.shortcuts import render, redirect
from django.views import View

from Petstagram.main.forms.pet_delete import PetDeleteForm
from Petstagram.main.models import PetModel


class DeletePetView(View):
    def get(self, req, pk):
        form = PetDeleteForm(instance=PetModel.objects.get(id=pk))
        return render(req, "pet_delete.html", {
            "form": form,
            "pk": pk
        })

    def post(self, req, pk):
        PetModel.objects.get(id=pk).delete()
        return redirect("/")
