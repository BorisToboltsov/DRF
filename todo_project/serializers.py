from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer

from todo_project.models import Project, ToDo


class ProjectModelSerializers(HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(view_name="user-detail", read_only=True,  many=True)

    class Meta:
        model = Project
        fields = "__all__"


class ToDoModelSerializers(HyperlinkedModelSerializer):
    user = HyperlinkedIdentityField(view_name="user-detail")
    project = HyperlinkedIdentityField(view_name="project-detail")

    class Meta:
        model = ToDo
        fields = "__all__"
