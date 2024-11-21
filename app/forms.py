from django import forms
from app.models import *


class CategoryMF(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'