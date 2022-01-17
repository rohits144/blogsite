from django_extensions.db.models import TimeStampedModel
from django.db import models


class Article(TimeStampedModel):

    title = models.CharField(null=False, blank=False, max_length=100)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def get_created(instance):
        return instance.created.strftime('%d-%m-%Y %H:%M')
    
    def get_modified(instance):
        return instance.modified.strftime('%d-%m-%Y %H:%M')

    def get_short_body(instance):
        if len(instance.body) < 1096:
            return instance.body + " ..."
        
        else:
            return instance.body[:1096] + " ..."

