from rest_framework import serializers
from energy_resources.models import EnergyResource
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    energy_resources = serializers.PrimaryKeyRelatedField(
        many=True, queryset=EnergyResource.objects.all())

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'energy_resources']
