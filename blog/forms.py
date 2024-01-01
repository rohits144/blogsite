from django.forms import ModelForm

from .models import Article, Comment
from django import forms

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'author', 'image']

class CommentForm(ModelForm):
    article_id = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Comment
        fields = ['username', 'body', 'article_id' ]
