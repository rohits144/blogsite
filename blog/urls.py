from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .views import ArticleListView, ArticleDetailView 
from django.views.generic.base import TemplateView  # Add this line
from blogsite import settings
from .views import ArticleCreateView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:pk>', ArticleDetailView.as_view(), name='article-detail'), 
    path('contact', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('create', ArticleCreateView.as_view(), name='article-create'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

