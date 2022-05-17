from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UsersModelSerializers


class UsersModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersModelSerializers
