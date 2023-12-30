from django_extensions.db.models import TimeStampedModel
from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class Article(TimeStampedModel):
    title = models.CharField(null=False, blank=False, max_length=100)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True, default='Cat03.jpg')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.EmailField(null=True, blank=True, max_length=100) 
    CATEGORY_CHOICES = [
        ('DEFAULT', 'Default'),
        ('FEEDS', 'Feeds'),
    ]

    category = models.CharField(null=False, blank=False, max_length=100, choices=CATEGORY_CHOICES, default='DEFAULT')

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


class Comment(TimeStampedModel):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    username = models.EmailField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.body[:50] + "..."
    
    @property
    def get_created(self):
        return self.created.strftime('%d-%m-%Y %H:%M')

    def clean(self):
        super().clean()
        validate_url = URLValidator()
        try:
            validate_url(self.body)
            raise ValidationError("Comments cannot contain URL links.")
        except ValidationError:
            pass

    def save(self, *args, **kwargs):
        if self.body is None or self.body == "":
            raise ValidationError("Comment body cannot be null.")
        super().save(*args, **kwargs)

        

