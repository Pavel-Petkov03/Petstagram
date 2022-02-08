from django.shortcuts import render
from django.views import View

from Petstagram.main.views.error_page import is_authenticated_decorator


class DeleteProfileView(View):
    @is_authenticated_decorator
    def get(self, req):
        return render(req, "profile_delete.html")

    def post(self):
        pass
