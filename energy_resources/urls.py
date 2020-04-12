from django.urls import path
from .views import EnergyResourcesList, EnergyResourceDetail

urlpatterns = [
    path('', EnergyResourcesList.as_view(), name='energy-resources-list'),
    path('<int:pk>/', EnergyResourceDetail.as_view(),
         name='energy-resource-details'),

]
