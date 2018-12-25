from django.urls import path

from website import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('pesee',views.pesee)
]