from django import forms
from app_nlp_news_classifier.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "article"
        ]
        labels = {"article": ""}