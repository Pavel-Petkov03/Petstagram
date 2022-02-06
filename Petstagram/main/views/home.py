from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, req):
        return render(req, "home_page.html")
