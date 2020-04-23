from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, unique=True)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(), related_name='articles', on_delete=models.CASCADE,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-details', kwargs={'slug': self.slug})


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(
        Article, related_name='comments', on_delete=models.CASCADE,)
    author = models.ForeignKey(
        get_user_model(), related_name='comments', on_delete=models.CASCADE,)

    def __str__(self):
        return self.comment
