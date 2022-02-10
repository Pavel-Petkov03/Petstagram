from django import forms

from Petstagram.main.models import PetModel


class PetCreateForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    date = forms.DateTimeField(widget=forms.SelectDateWidget())

    class Meta:
        model = PetModel
        fields = "__all__"


