from django.template.defaulttags import url
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register(r'categories', CategoryModelViewSet)
router.register(r'tags', TagModelViewSet)
router.register(r'training', TrainingModelViewSet)

urlpatterns = [
    path('/', include(router.urls)),
]
