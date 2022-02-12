from django.shortcuts import render
from django.views import View

from Petstagram.main.forms.pet_photo import PetImageForm
from Petstagram.main.models import PetModel, ProfileModel


class AddPhotoView(View):
    def get(self, req):
        form = PetImageForm()
        options = list(PetModel.objects.filter(user_profile=ProfileModel.objects.first()).values("name"))
        print(options)
        form.fill_choices(options)
        return render(req, "photo_create.html", {
            "form": form
        })
