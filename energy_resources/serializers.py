from rest_framework import serializers
from .models import EnergyResource
from django.contrib.auth import get_user_model


class EnergyResourceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    net_energy = serializers.ReadOnlyField()
    class Meta:
        model = EnergyResource
        fields = ['id', 'resource_type',
                  'status', 'location', 'capacity', 'consumption', 'net_energy', 'owner']
