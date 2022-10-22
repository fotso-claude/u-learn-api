from rest_framework import serializers

from src.login.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ['id', 'name', 'email', 'password', 'role']