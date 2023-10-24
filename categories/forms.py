from django import forms
from .models import Categories
from colorfield.widgets import ColorWidget
from colorfield.fields import ColorField


class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ["title", "bg_color", "author", "image"]


class UpdateCategory(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ["title", "bg_color", "author", "image"]
