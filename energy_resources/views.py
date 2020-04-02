from .serializers import EnergyResourceSerializer, UserSerializer
from rest_framework import generics, permissions
from .models import EnergyResource
from django.contrib.auth import get_user_model
from .permissions import IsOwnerOrReadOnly


class EnergyResourcesList(generics.ListCreateAPIView):
    queryset = EnergyResource.objects.all()
    serializer_class = EnergyResourceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EnergyResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnergyResource.objects.all()
    serializer_class = EnergyResourceSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UsersList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
