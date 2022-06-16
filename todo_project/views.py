from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from todo_project.models import Project, ToDo
from todo_project.serializers import ProjectModelSerializers, ToDoModelSerializers


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializers


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializers
