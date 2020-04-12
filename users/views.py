from rest_framework import generics, permissions
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

# Create your views here.

class UsersList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
