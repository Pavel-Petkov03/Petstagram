from django.shortcuts import render
from django.views import View

from Petstagram.main.forms.profile_create import CreateProfileForm
from Petstagram.main.views.error_page import check_if_has_profile


class ProfileView(View):
    def get(self, req):
        if check_if_has_profile():
            return render(req , "profile_details.html")
        else:
            form = CreateProfileForm()
            return render(req, "profile_create.html", {
                "form": form
            })
