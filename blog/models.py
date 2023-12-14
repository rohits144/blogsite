from django_extensions.db.models import TimeStampedModel
from django.db import models


class Article(TimeStampedModel):
    
    title = models.CharField(null=False, blank=False, max_length=100)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.CharField(null=False, blank=False, max_length=100) 

    @property
    def get_created(self):
        return self.created.strftime('%d-%m-%Y %H:%M')
    
    @property
    def get_modified(self):
        return self.modified.strftime('%d-%m-%Y %H:%M')

    def __str__(self):
        return self.title
    
    @property
    def get_small_title(self):
        return self.title[:10] + "..."
    
    @property
    def get_author(self):
        return self.author
    
    @property
    def get_short_description(self):
        return self.body[:100] + "..."

    

        




