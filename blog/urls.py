from django.contrib import admin
from django.urls import path, include

from .views import ListArticles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListArticles.as_view())
]