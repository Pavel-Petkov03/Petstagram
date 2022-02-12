from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Petstagram.main.views.create_pet import CreatePetView
from Petstagram.main.views.create_photo import AddPhotoView
from Petstagram.main.views.create_profile import ProfileView
from Petstagram.main.views.delete_pet import DeletePetView
from Petstagram.main.views.delete_profile import DeleteProfileView
from Petstagram.main.views.edit_pet import EditPetView
from Petstagram.main.views.edit_profile import EditProfileView
from Petstagram.main.views.home import HomeView

urlpatterns = [
                  path("", HomeView.as_view(), name="home"),
                  path("profile", ProfileView.as_view(), name="profile"),
                  path("profile/edit", EditProfileView.as_view(), name="profile-edit"),
                  path("profile/delete", DeleteProfileView.as_view(), name="profile-delete"),
                  path("pet/create", CreatePetView.as_view(), name="pet-create"),
                  path("pet/edit/<int:pk>", EditPetView.as_view(), name="pet-edit"),
                  path("pet/delete/<int:pk>", DeletePetView.as_view(), name="pet-delete"),
                  path("photo/create", AddPhotoView.as_view(), name="photo-create")
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
