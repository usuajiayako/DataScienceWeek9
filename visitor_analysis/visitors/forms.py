from django import forms
from . import models

class RegisterVisitor(forms.ModelForm):
    class Meta:
        model = models.Visitor
        fields = ['age', 'gender'] # deleted 'thumb'

