from django.shortcuts import render
from django.views import View


class EditPhotoView(View):
    def get(self, req):
        return render(req, "photo_edit.html")

    def post(self):
        pass
