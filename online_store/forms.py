from django import forms
from . import models

class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['image', 'phone', 'address']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)
        