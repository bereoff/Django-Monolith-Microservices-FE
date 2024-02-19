from rest_framework.serializers import ModelSerializer

from .models import CustomUser


class UsersSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "password",
            "email"
        ]
