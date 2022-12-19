from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from login.models import Auth
from training.serializers import TrainingSerializer


class AuthSerializer(serializers.ModelSerializer):
    training = TrainingSerializer(many=True, read_only=True)

    class Meta:
        model = Auth
        fields = ('id', 'last_name', 'username', 'email', 'role', 'training')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Auth.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        model = Auth
        fields = '__all__'
        extra_kwargs = {
            'username': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'password': {'required': True, 'write_only': True},
        }

        def create(self, validated_data):
            user = Auth.objects.create(
                username=validated_data['username'],
                last_name=validated_data['last_name'],
                email=validated_data['email'],
                is_active=1,
                password=make_password(validated_data['password']),
            )
            user.save()
            return user
