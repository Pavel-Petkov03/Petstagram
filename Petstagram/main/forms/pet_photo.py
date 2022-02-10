from django import forms

from Petstagram.main.models import PetImage


class PetImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput())
    tagged_pets = forms.MultipleChoiceField(widget=forms.SelectMultiple())
    description = forms.CharField(widget=forms.Textarea())

    def fill_choices(self, choices):
        self.fields["tagged_pets"].choices = [(choice, choice) for choice in choices]

    class Meta:
        model = PetImage
        fields = ["image", "tagged_pets", "description"]
