from rest_framework import serializers
from .models import EnergyResource
from django.contrib.auth import get_user_model


class EnergyResourceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = EnergyResource
        fields = ['id', 'resource_type',
                  'status', 'location', 'capacity', 'owner']
