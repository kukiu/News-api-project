from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'source_name', 'author', 'title', 'description', 
                 'url', 'url_to_image', 'published_at', 'content'] 