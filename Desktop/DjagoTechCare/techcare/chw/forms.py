from django import forms
from django.forms.widgets import Widget
from .models import Households

class HouseholdRegistrationForm(forms.ModelForm):
    class Meta:
        model = Households
        fields ="__all__"
       