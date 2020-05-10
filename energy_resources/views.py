from .serializers import EnergyResourceSerializer
from rest_framework import generics
from .models import EnergyResource
from .permissions import IsOwnerOrReadOnly


class EnergyResourcesList(generics.ListCreateAPIView):
    queryset = EnergyResource.objects.all()
    serializer_class = EnergyResourceSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EnergyResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnergyResource.objects.all()
    serializer_class = EnergyResourceSerializer
    permission_classes = [IsOwnerOrReadOnly, ]
