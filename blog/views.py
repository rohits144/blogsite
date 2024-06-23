from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView
from rest_framework import generics

from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from django.contrib import messages


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'article_list.html'
    paginate_by = 5
    queryset = Article.objects.filter().order_by('-created')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['all_articles'] = Article.objects.filter().order_by('created')[:10]
        return context


class ArticleDetailView(DetailView, generics.CreateAPIView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['comments'] = Article.get_all_comments(article)
        return context


class InstaFeed(TemplateView):
    template_name = 'insta_feeds.html'


class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    form_class = ArticleForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'article_create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.image = form.cleaned_data['image']
            article.save()
            messages.success(request, 'Article created successfully.')
            return HttpResponseRedirect(reverse('article-list'))
        else:
            return render(request, 'article_create.html', {'form': form, 'error_message': 'Invalid form data'})


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            article_id = form.cleaned_data['article_id']
            comment.article = Article.objects.get(pk=article_id)
            comment.save()
            messages.success(request, 'Comment created successfully.')
            return HttpResponseRedirect(reverse('article-detail', kwargs={'pk': article_id}))


class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
