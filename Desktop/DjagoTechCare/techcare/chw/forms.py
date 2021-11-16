from django import forms
from django.forms.widgets import Widget
from .models import Households,Referral

class HouseholdRegistrationForm(forms.ModelForm):
    class Meta:
        model = Households
        fields ="__all__"
       


class ReferralRegistrationForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields ="__all__"