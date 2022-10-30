from django.template.defaulttags import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from knox import views as knox_views

from .views import *

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
