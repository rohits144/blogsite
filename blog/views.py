
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from rest_framework import generics

from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Article

class ArticleListView(TemplateView):
    template_name = 'article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs.get('category', "DEFAULT")
        articles = Article.objects.filter(category=category).order_by('-created')
        context['category'] = category
        context['articles'] = articles
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
        else:
            return HttpResponseRedirect(reverse('article-detail', kwargs={'pk': article_id, 'error_message': 'Invalid form data'}))

