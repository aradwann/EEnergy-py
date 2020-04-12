from django.urls import path
from .views import UserDetail, UsersList

urlpatterns = [
    path('', UsersList.as_view(), name='users-list'),
    path('<int:pk>/', UserDetail.as_view(),
         name='user-details'),
]
