from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Article
        fields = ['id', 'title',
                  'body', 'author', 'comments', 'created_date']
