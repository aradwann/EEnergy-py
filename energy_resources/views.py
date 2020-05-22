from . import serializers
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import EnergyResource
from .permissions import IsOwnerOrReadOnly

from django.contrib.gis.db.models.functions import Distance


class EnergyResourcesViewSet(viewsets.ModelViewSet):
    """View set for energy resource model"""
    queryset = EnergyResource.objects.all()
    serializer_class = serializers.EnergyResourceSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]

    def get_queryset(self):
        """return energy resource objects available"""
        return EnergyResource.objects.all()

    def perform_create(self, serializer):
        """Create a new energy resource"""
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'retrieve':
            return serializers.EnergyResourceDetailSerializer
        elif self.action == 'nearby':
            return serializers.NearbyEnergyResourceSerializer

        return self.serializer_class

    @action(methods=['GET'], detail=True)
    def nearby(self, request, pk=None):
        """get nearby energy resources to
            the current energy resource in detail"""
        energy_resource = self.get_object()
        # the distance is returned in metres
        # lte means less than or equal
        energy_resources = EnergyResource.objects.annotate(
            distance=Distance('location', energy_resource.location)
        ).filter(distance__lte=1000).order_by('distance')[0:3]
        serializer = self.get_serializer(
            energy_resources, many=True)
        return Response(serializer.data)
