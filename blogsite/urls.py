
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from blog import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(blog_urls), name='articles'),
]
