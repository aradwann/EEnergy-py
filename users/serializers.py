from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    """serialize user instance"""

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']
