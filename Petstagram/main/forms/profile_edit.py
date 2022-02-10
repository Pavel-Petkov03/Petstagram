from Petstagram.main.forms.profile_create import CreateProfileForm
from django import forms
from django.forms import SelectDateWidget


class ProfileEditForm(CreateProfileForm):
    date_of_birth = forms.DateField(widget=SelectDateWidget(attrs={
        "style": "display:block;width:100%;padding:8px"
    }))

    description = forms.CharField(widget=forms.Textarea({
        "style": "display:block", "rows": 5, "cols": 70
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "style": "display:block"
    }))
    profile_picture = forms.URLField(widget=forms.URLInput())

    # gender = forms.ChoiceField(widget=forms.Select(attrs={}))
    class Meta(CreateProfileForm.Meta):
        fields = "__all__"
