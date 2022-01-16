from turtle import title
from django.db import models

class Article(models.Model):

    title = models.CharField(null=False, blank=False, max_length=100)
    body = models.TextField()
    image = models.ImageField('blog_image')
