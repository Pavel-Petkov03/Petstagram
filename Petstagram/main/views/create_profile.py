from django.shortcuts import render, redirect
from django.views import View

from Petstagram.main.forms.profile_create import CreateProfileForm
from Petstagram.main.models import ProfileModel, PetImage, PetModel
from Petstagram.main.views.error_page import check_if_has_profile


class ProfileView(View):
    def get(self, req):
        if check_if_has_profile():
            profile = ProfileModel.objects.all()[0]
            total_images = PetImage.objects.all()
            total_likes = sum([image.likes for image in total_images])
            total_pets = PetModel.objects.all()
            return render(req, "profile_details.html",
                          {"profile": profile, "likes": total_likes, "images": total_images.__len__()}, "total_pets",
                          total_pets)
        form = CreateProfileForm()
        return render(req, "profile_create.html", {
            "form": form
        })

    def post(self, req):
        form = CreateProfileForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(req, "profile_create.html", {"form": form})
