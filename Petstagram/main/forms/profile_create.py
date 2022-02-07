from django import forms
from Petstagram.main.models.profile import ProfileModel
from Petstagram.main.validators.name_validator import NameValidator


class CreateProfileForm(forms.ModelForm):
    FIRST_NAME_MIN_LENGTH = 2
    SECOND_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    SECOND_NAME_MAX_LENGTH = 30
    first_name = forms.CharField(label="First Name", max_length=30, widget=forms.TextInput(attrs={
        "type": "text", "class": "form-control", "name": "first_name", "maxlength": 30, "required": True,
        "placeholder": "Enter first name", "id": "first_name"
    }), validators=[
        NameValidator(FIRST_NAME_MIN_LENGTH, FIRST_NAME_MAX_LENGTH, "first name")
    ])
    last_name = forms.CharField(label="Last Name", max_length=30, widget=forms.TextInput(attrs={
        "type": "text", "class": "form-control", "name": "second_name", "maxlength": 30, "required": True,
        "placeholder": "Enter second name", "id": "id_last_name"
    }), validators=[
        NameValidator(SECOND_NAME_MIN_LENGTH, SECOND_NAME_MAX_LENGTH, "second name")
    ])
    profile_picture = forms.URLField(label="Link to Profile Image", max_length=30, widget=forms.URLInput(attrs={
        "type": "url", "class": "form-control", "name": "profile_image", "maxlength": 30, "required": True,
        "placeholder": "Enter URL", "id": "id_image"
    }))

    class Meta:
        fields = "__all__"
        model = ProfileModel
