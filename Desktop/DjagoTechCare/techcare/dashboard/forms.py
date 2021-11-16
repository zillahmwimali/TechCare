from django import forms
from django.forms.widgets import Widget
from chw.models import Chw
from .models import OrgProfile

class ChwRegistrationForm(forms.ModelForm):
    class Meta:
        model = Chw
        fields ="__all__"


class EditProfileForm(forms.ModelForm):

    class Meta:
        model=OrgProfile
        fields="__all__"