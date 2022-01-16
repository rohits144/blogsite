from django.shortcuts import render
from rest_framework import generics

from .models import Article
from .serializers import ArticleSerializer

class ListArticles(generics.ListAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer


