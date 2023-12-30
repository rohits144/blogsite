from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from rest_framework import generics

from .forms import ArticleForm
from .models import Article
from .serializers import ArticleSerializer
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


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

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
