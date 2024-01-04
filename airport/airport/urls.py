"""Urls of all project."""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('airline/', include('base.airline_urls')),
    path('aircraft/', include('base.aircraft_urls')),
    path('api-token-auth/', include('base.auth_urls')),
]
