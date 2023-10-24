from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "description",
                  "series", "author", "image", "content"]


class UpdateArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = fields = ["title", "description",
                           "series", "author", "image", "content"]
