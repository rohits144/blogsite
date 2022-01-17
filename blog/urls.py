from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .views import ListArticles
from blogsite import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListArticles.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
