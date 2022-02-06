from django.shortcuts import render
from django.views import View


class CreateProfileView(View):
    def get(self, req):
        # going to make form
        return render(req, "profile_create.html")
