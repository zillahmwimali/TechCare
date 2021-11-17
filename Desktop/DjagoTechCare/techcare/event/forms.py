from django import forms
from django.forms import ModelForm, DateInput
from django.forms.widgets import TextInput
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        # datetime-local is a HTML5 input type, format to make date time show on fields
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'organizer':forms.TextInput(attrs={'class': 'form-control'}),
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'description': forms.Textarea(attrs={'class': 'form_control', 'id': 'des'}),

        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
