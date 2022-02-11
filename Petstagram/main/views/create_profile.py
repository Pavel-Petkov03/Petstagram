from django.shortcuts import render, redirect
from django.views import View

from Petstagram.main.forms.profile_create import CreateProfileForm
from Petstagram.main.models import ProfileModel, PetImage, PetModel
from Petstagram.main.views.error_page import check_if_has_profile


class ProfileView(View):
    def get(self, req):
        if check_if_has_profile():
            profile = ProfileModel.objects.first()
            pets = list(PetModel.objects.filter(user_profile=profile))
            pet_photos = PetImage.objects.filter(tagged_pets__petimage__photo__in=pets)
            total_likes = sum([photo.likes for photo in pet_photos])
            context = {"profile": profile, "likes": total_likes, "images": pet_photos.__len__(),
                       "total_pets": pets}
            return render(req, "profile_details.html", context)
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



