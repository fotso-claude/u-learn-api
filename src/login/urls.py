from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('users/', views.user_list),
    path('user/create/', views.user_create),
    path('user/<int:id>', views.user_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)