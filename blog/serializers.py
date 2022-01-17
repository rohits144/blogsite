from imp import source_from_cache
from urllib import request
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):

    created = serializers.CharField(source='get_created')
    modified = serializers.CharField(source='get_modified')
    short_body = serializers.CharField(source='get_short_body')
    image = serializers.SerializerMethodField()

    class Meta:
        model=Article
        fields= ['id', 'title', 'short_body', 'body', 'image', 'created', 'modified']

    def get_image(self, instance):
        if not instance.image:
            return False
        else:
            request = self.context.get('request')
            return request.build_absolute_uri("/media/" + instance.image.name)