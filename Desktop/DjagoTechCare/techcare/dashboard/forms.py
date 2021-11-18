from django import forms
from django.forms.widgets import Widget
from core.models import Chw

class ChwRegistrationForm(forms.ModelForm):
    class Meta:
        model = Chw
        fields ="__all__"
       