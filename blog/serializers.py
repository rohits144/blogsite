from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):

    created = serializers.CharField(source='get_created')
    modified = serializers.CharField(source='get_modified')
    short_body = serializers.CharField(source='get_short_body')

    class Meta:
        model=Article
        fields= ['id', 'title', 'short_body', 'body', 'image', 'created', 'modified']

