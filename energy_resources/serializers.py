from rest_framework import serializers
from .models import EnergyResource


class EnergyResourceSerializer(serializers.ModelSerializer):
    """Model serializer for energy resource instance"""
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = EnergyResource
        fields = ['id', 'resource_type',
                  'status', 'location',
                  'capacity', 'consumption',
                  'net_energy', 'owner']
        read_only_fields = ['id', 'owner', 'net_energy']
