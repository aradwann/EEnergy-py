from rest_framework import serializers
from .models import EnergyResource
from users.serializers import UserSerializer


class EnergyResourceSerializer(serializers.ModelSerializer):
    """list serializer for energy resource instances"""
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = EnergyResource
        fields = ['id', 'resource_type',
                  'status', 'location',
                  'capacity', 'consumption',
                  'net_energy', 'owner']
        read_only_fields = ['id', 'owner', 'net_energy']


class EnergyResourceDetailSerializer(EnergyResourceSerializer):
    """detail serializer for energy resource instance"""
    owner = UserSerializer()


class NearbyEnergyResourceSerializer(serializers.ModelSerializer):
    """nearby energy resource serializer for energy resource instance"""
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    distance = serializers.FloatField()

    class Meta:
        model = EnergyResource
        fields = ['id', 'net_energy', 'owner', 'distance']
        read_only_fields = ['id', 'owner', 'net_energy', 'distance']
