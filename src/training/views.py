from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS

from rest_framework.viewsets import ModelViewSet

from training.models import Training, Category, Tag
from training.serializers import TrainingSerializer, CategorySerializer, TagSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class CategoryModelViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagModelViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TrainingModelViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    # parser_classes = (MultiPartParser, FormParser)
    #  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
