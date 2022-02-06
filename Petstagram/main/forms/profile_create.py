from django import forms


# <form>
#                 <div class="form-group">
#                     <label for="first_name">First Name</label>
#                     <input type="text" class="form-control" name="first_name" maxlength="30" required
#                            placeholder="Enter first name" id="first_name"/>
#                 </div>
#                 <div class="form-group">
#                     <label for="id_last_name">Last Name</label>
#                     <input type="text" class="form-control" name="last_name" maxlength="30" required
#                            placeholder="Enter last name" id="id_last_name"/>
#                 </div>
#                 <div class="form-group">
#                     <label for="id_image">Link to Profile Image</label>
#                     <input type="url" class="form-control" name="profile_image" required id="id_image"
#                     placeholder="Enter URL"/>
#                 </div>
#                 <button class="btn btn-primary mt-2" type="submit">Create</button>
#             </form>
from Petstagram.main.models.profile import ProfileModel
from Petstagram.main.validators.name_validator import NameValidator


class CreateProfileForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", max_length=30, widget=forms.TextInput(attrs={
        "type": "text", "class": "form-control", "name": "first_name", "maxlength": 30, "required": True,
        "placeholder": "Enter first name", "id": "first_name"
    }), validators=[

    ])
    last_name = forms.CharField(label="Last Name", max_length=30, widget=forms.TextInput(attrs={
        "type": "text", "class": "form-control", "name": "second_name", "maxlength": 30, "required": True,
        "placeholder": "Enter second name", "id": "id_last_name"
    }))
    profile_picture = forms.URLField(label="Link to Profile Image", max_length=30, widget=forms.URLInput(attrs={
        "type": "url", "class": "form-control", "name": "profile_image", "maxlength": 30, "required": True,
        "placeholder": "Enter URL", "id": "id_image"
    }))

    class Meta:
        fields = "__all__"
        model = ProfileModel
