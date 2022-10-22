from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list),
    path('user/create/', views.user_create),
    path('user/<int:id>', views.user_detail),
]
