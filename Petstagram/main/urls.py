from django.urls import path

from Petstagram.main.views.create_profile import ProfileView
from Petstagram.main.views.home import HomeView

urlpatterns = [
    path("", HomeView.as_view()),
    path("create", ProfileView.as_view()),
]