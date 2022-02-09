from Petstagram.main.forms.profile_create import CreateProfileForm


class ProfileEditForm(CreateProfileForm):
    class Meta(CreateProfileForm.Meta):
        fields = "__all__"
