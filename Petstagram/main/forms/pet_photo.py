from django import forms

from Petstagram.main.models import PetImage


class PetImageForm(forms.ModelForm):

    class Meta:
        model = PetImage
