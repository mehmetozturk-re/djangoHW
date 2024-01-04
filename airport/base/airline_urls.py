"""This file includes Airline CRUD urls."""
from django.urls import path
from . import views

# CLASS VIEWS

urlpatterns = [
    path('', views.AirlineGetListCreateAPIView.as_view()),
    path('<int:id>', views.AirlineGetDeleteUpdateByIdAPIView.as_view()),
]

# FUNCTION BASED VIEWS

# Ilk once Function Base yaptigim islemleri, arastirmalarimin sonucunda
# daha kullanisli olarak buldugum Class Base hale cevirdim ve daha sonrasinda
# projenin kalanina boyle devam ettim. Function Base halini yaptigim kisimlari
# ise yorum olarak goruslerinize birakiyorum.

# urlpatterns = [
#    path('', views.airline_get_list_create),
#    path('<int:id>', views.airline_get_delete_update_by_id),
# ]
