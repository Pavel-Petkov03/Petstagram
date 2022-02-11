from Petstagram.main.forms.pet_create import PetCreateForm


class PetDeleteForm(PetCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()

    def disable_fields(self):
        for field in self.fields:
            self.fields[field].widget.attrs["disabled"] = True
