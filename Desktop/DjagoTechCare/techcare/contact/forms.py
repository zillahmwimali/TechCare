from django import forms
from django.forms.widgets import Widget
from .models import Contact
 
class ContactForm(forms.ModelForm):
   class Meta:
       model = Contact
       fields ="__all__"