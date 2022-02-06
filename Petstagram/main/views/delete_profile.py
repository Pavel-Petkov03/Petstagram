from django.shortcuts import render
from django.views import View


class DeleteProfileView(View):
    def get(self, req):
        return render(req, "profile_delete.html")

    def post(self):
        pass
