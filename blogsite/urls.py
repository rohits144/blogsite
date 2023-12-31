
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from blogsite import settings

from blog import urls as blog_urls
from tasks import urls as tasks_urls  # Import the tasks URLs


urlpatterns = [
    path('tasks/', include(tasks_urls)),
    path('rohit_login/', admin.site.urls),
    path('', include(blog_urls), name='articles'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)