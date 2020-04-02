from django.urls import path
from .views import EnergyResourcesList, EnergyResourceDetail, UserDetail, UsersList

urlpatterns = [
    path('', EnergyResourcesList.as_view(), name='energy-resources-list'),
    path('<int:pk>/', EnergyResourceDetail.as_view(),
         name='energy-resource-details'),
    path('users/', UsersList.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetail.as_view(),
         name='user-details'),
]