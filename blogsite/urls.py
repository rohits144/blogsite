
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from blogsite import settings

from blog import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(blog_urls), name='articles'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)