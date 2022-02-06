from django.shortcuts import render
from django.views import View

from Petstagram.main.forms.profile_create import CreateProfileForm


class CreateProfileView(View):
    def get(self, req):
        form = CreateProfileForm()
        return render(req, "profile_create.html", {
            "form": form
        })
