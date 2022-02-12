from django import forms

from Petstagram.main.models import PetImage


class PetImageForm(forms.ModelForm):
    tagged_pets = forms.MultipleChoiceField(widget=forms.SelectMultiple())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def fill_choices(self, choices):
        new_choices = [(choice["name"], choice["name"]) for choice in choices]
        self.fields["tagged_pets"].choices = new_choices

    class Meta:
        model = PetImage
        fields = ["photo", "description", "tagged_pets"]
        widgets = {
            "photo": forms.FileInput(attrs={
                "type": "file", "id": "file-upload", "name": "filename", "class": "form-control-file"
            }),
            "description": forms.Textarea(attrs={
                "type": "text", "id": "first_name", "name": "first_name", "placeholder": "Enter Description",
                "rows": 3, "class": "form-control"
            })
        }

        labels = {
            "description": "Description",
            "photo": "Pet Image"
        }
