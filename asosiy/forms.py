from django import forms
from.models import *

class KundalikForm(forms.ModelForm):
    class Meta:
        model =Kundalik
        fields = "__all__"