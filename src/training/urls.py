from django.template.defaulttags import url
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register(r'categories', CategoryModelViewSet, basename='categories')
router.register(r'tags', TagModelViewSet, basename='tags')
router.register(r'training', TrainingModelViewSet, basename='training')

urlpatterns = [
    path('/', include(router.urls)),
]
