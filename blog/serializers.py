from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='get_author')
    created = serializers.CharField(source='get_created')
    modified = serializers.CharField(source='get_modified')
    small_title = serializers.CharField(source='get_small_title')
    image = serializers.SerializerMethodField()

    class Meta:
        model=Article
        fields= ['id', 'title', 'small_title', 'body', 'image', 'created', 'modified', 'author']

    def get_image(self, instance):
        if not instance.image:
            return False
        else:
            request = self.context.get('request')
            return request.build_absolute_uri("/media/" + instance.image.name)

    def validate_title(self, value):
        # Add custom validation logic for the title field
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

