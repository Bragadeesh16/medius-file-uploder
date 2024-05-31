from django import forms
from .models import *

class file_form(forms.Form):
    file = forms.FileField()
