from django.urls import path

from Petstagram.main.views.home import HomeView

urlpatterns = [
    path("", HomeView.as_view())
]