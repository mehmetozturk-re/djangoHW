"""This file includes Aircraft CRUD urls."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AircraftCreateAPIView.as_view()),
    path('<int:id>', views.AircraftGetDeleteUpdateByIdAPIView.as_view()),
]
