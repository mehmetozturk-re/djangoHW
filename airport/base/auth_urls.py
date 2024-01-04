"""This file includes User CRUD urls."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserObtainTokenAPIView.as_view())
]
