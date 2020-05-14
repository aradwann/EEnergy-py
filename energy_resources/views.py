from .serializers import EnergyResourceSerializer
from rest_framework import viewsets, permissions
from .models import EnergyResource
from .permissions import IsOwnerOrReadOnly


class EnergyResourcesViewSet(viewsets.ModelViewSet):
    """View set for energy resource model"""
    queryset = EnergyResource.objects.all()
    serializer_class = EnergyResourceSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]

    def get_queryset(self):
        """return energy resource objects available"""
        return EnergyResource.objects.all()

    def perform_create(self, serializer):
        """Create a new energy resource"""
        serializer.save(owner=self.request.user)
