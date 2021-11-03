from django import forms
from django.forms.widgets import Widget
from chw.models import Chw

class ChwRegistrationForm(forms.ModelForm):
    class Meta:
        model = Chw
        fields ="__all__"
       