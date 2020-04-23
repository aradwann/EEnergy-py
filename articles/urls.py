from django.urls import path
from .views import ArticleDetail, ArticlesList

urlpatterns = [
    path('', ArticlesList.as_view(), name='articles-list'),
    path('<slug:slug>/', ArticleDetail.as_view(),
         name='article-details'),

]
