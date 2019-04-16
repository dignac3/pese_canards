from django.urls import path

from website import views

urlpatterns = [
    path('', views.pesee),
    path('index', views.pesee,name="accueil"),

    path('telechargements',views.telechargements, name="telechargements"),

    #Pesee
    path('pesee',views.pesee,name="pesee"),
    path('pesee/start',views.startPesee,name="start_pesee"),
    path('pesee/stop',views.stopPesee, name="stop_pesee"),
    path('pesee/<int:pesee_id>/delete',views.deletePesee),
    path('pesee/<int:pesee_id>/fichier',views.downloadFile),
    path('pesee/restart', views.restartPesee),
    path('pesee/cancel', views.cancelPesee),



]