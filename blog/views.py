from django.shortcuts import render
from rest_framework import generics

from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView, DetailView
from .models import Article


class ArticleListView(TemplateView):
    template_name = 'article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.all().order_by("-created")
        context['articles'] = articles
        return context



class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'



