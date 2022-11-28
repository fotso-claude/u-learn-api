from django.shortcuts import render
from rest_framework.decorators import action

from rest_framework.viewsets import ModelViewSet

from training.models import Training, Category, Tag
from training.serializers import TrainingSerializer, CategorySerializer, TagSerializer
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagModelViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TrainingModelViewSet(ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    # parser_classes = (MultiPartParser, FormParser)
    #  permission_classes = [permissions.IsAuthenticatedOrReadOnly]


