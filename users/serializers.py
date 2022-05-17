from rest_framework.serializers import HyperlinkedModelSerializer

from users.models import User


class UsersModelSerializers(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
