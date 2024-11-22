from django import forms
from app.models import *


class CategoryMF(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class SchoolForm(forms.ModelForm):
    class Meta:
        model=School
        fields='__all__'
        



