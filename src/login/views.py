from django.contrib.auth import login
from knox.models import AuthToken
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.response import Response

from .models import Auth
from .serializers import RegisterSerializer, AuthSerializer


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        return Response({
            "user": AuthSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user = Auth.objects.get(username=user.username)
        login(request, user)
        temp_list = super(LoginAPI, self).post(request, format=None)
        temp_list.data['is_admin'] = user.is_staff
        temp_list.data['user'] = {
            "username": user.username,
            "last_name": user.last_name,
            "email": user.email,
            "role": user.role
        }
        return Response({'datas': temp_list.data})

