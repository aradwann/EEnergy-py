from .serializers import EnergyResourceSerializer, UserSerializer
from rest_framework import generics
from .models import EnergyResource
from django.contrib.auth import get_user_model 


class EnergyResourcesList(generics.ListCreateAPIView):
    queryset = EnergyResource.objects.all()
    serializer_class = EnergyResourceSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EnergyResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnergyResource.objects.all()
    serializer_class = EnergyResourceSerializer



class UsersList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer