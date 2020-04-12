from django.db import models
from django.contrib.auth import get_user_model


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(), related_name='articles', on_delete=models.CASCADE,)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(
        Article, related_name='comments', on_delete=models.CASCADE,)
    author = models.ForeignKey(
        get_user_model(), related_name='comments', on_delete=models.CASCADE,)

    def __str__(self):
        return self.comment
