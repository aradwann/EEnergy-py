from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Article
        fields = ['id', 'title',
                  'body', 'author', 'comments','created_date' ]

