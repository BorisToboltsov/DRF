from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UsersModelSerializer


class UsersModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersModelSerializer
