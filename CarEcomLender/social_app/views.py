from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import User
from .serializers import UserSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserListUpdate(generics.UpdateAPIView):

    serializer_class = UserSerializer