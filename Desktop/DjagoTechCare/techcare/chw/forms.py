from django import forms
from django.forms.widgets import Widget
from .models import Households, Mother_referral,Referral,MotherAssessment,GeneralAssessment,ChildAssessment,Mother_referral

class HouseholdRegistrationForm(forms.ModelForm):
    class Meta:
        model = Households
        fields ="__all__"

class ReferralAssessmentForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields ="__all__"

class MotherAssessmentForm(forms.ModelForm):
    class Meta:
        model = MotherAssessment
        fields ="__all__"

class GeneralAssessmentForm(forms.ModelForm):
    class Meta:
        model = GeneralAssessment
        fields ="__all__"

class ChildAssessmentForm(forms.ModelForm):
    class Meta:
        model = ChildAssessment
        fields ="__all__"

class MotherReferralForm(forms.ModelForm):
    class Meta:
        model = Mother_referral
        fields ="__all__"