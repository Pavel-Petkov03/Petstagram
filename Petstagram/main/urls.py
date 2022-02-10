from django.urls import path

from Petstagram.main.views.create_pet import CreatePetView
from Petstagram.main.views.create_profile import ProfileView
from Petstagram.main.views.delete_profile import DeleteProfileView
from Petstagram.main.views.edit_pet import EditPetView
from Petstagram.main.views.edit_profile import EditProfileView
from Petstagram.main.views.home import HomeView

urlpatterns = [
    path("", HomeView.as_view()),
    path("profile", ProfileView.as_view()),
    path("profile/edit", EditProfileView.as_view()),
    path("profile/delete", DeleteProfileView.as_view()),
    path("pet/create", CreatePetView.as_view()),
    path("pet/edit/<int:pk>", EditPetView.as_view())
]
