from django import forms

from Petstagram.main.models import PetModel


class PetCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fill_fields()

    def fill_fields(self):
        for (_, field) in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = PetModel
        fields = ["name", "type", "date"]
        labels = {
            "name": "Pet Name",
            "type": "Type:",
            "date": "Day of Birth:",
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "type": "text", "name": "first_name", "placeholder": "Enter name", "id": "name"
            }),
            "type": forms.Select(),
            "date": forms.DateTimeInput(attrs={
                "type": "date", "name": "age", "id": "age"
            })
        }
