from django import forms
from .models  import Meeting, Minute, Resource, event

class meetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'




