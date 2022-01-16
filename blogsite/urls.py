
from django.contrib import admin
from django.urls import path, include

from blog import urls as article_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(article_urls), name='articles')
]
