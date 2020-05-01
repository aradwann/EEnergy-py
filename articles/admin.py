from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.TabularInline):

    model = Comment


class ArticleAdmin(admin.ModelAdmin):

    inlines = [
        CommentInline,
    ]

    list_display = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
