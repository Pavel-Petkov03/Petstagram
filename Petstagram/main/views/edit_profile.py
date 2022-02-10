from django.shortcuts import render, redirect
from django.views import View

from Petstagram.main.forms.profile_edit import ProfileEditForm
from Petstagram.main.models import ProfileModel
from Petstagram.main.views.error_page import is_authenticated_decorator


class EditProfileView(View):
    @is_authenticated_decorator
    def get(self, req):
        form = ProfileEditForm(instance=ProfileModel.objects.first())
        return render(req, "profile_edit.html", {
            "form": form
        })

    @is_authenticated_decorator
    def post(self, req):
        form = ProfileEditForm(req.POST, instance=ProfileModel.objects.first())
        if form.is_valid():
            form.save()
            return redirect("/")
        return render(req, "profile_edit.html", {
            "form": form
        })
