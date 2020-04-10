from rest_framework import serializers
from .models import EnergyResource
from django.contrib.auth import get_user_model


class EnergyResourceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = EnergyResource
        fields = ['id', 'resource_type',
                  'status', 'location', 'capacity', 'owner']


class UserSerializer(serializers.ModelSerializer):
    energy_resources = serializers.PrimaryKeyRelatedField(
        many=True, queryset=EnergyResource.objects.all())

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'energy_resources']
