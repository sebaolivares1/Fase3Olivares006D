from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tutorialdestiny/', views.tuDestiny, name='tuDestiny'),
    path('tutorialsea/', views.tuSea, name='tuSea'),
    path('videos/', views.videos, name='videos'),
    path('administrar/', views.agjuegos, name='agjuegos'),
    path('juego/<int:pk>', views.JuegoDetailView.as_view(), name='juego-detail'),
    path('juegos/', views.JuegoListView.as_view(), name='juegos'),
    path('adm/', views.index_admin, name='index_admin'),
    path('user/', views.index_user, name='index_user'),
    path('tuto/<int:pk>', views.JuegoInstanceDetailView.as_view(), name='juegoinstance-detail'),
    path('tutos/', views.JuegoInstanceListView.as_view(), name='tutos'),
   
]

urlpatterns+=[
    path('juego/create/', views.JuegoCreate.as_view(), name='juego_create'),
    path('juego/<int:pk>/update/', views.JuegoUpdate.as_view(), name='juego_update'),
    path('juego/<int:pk>/delete/', views.JuegoDelete.as_view(), name='juego_delete'),
    path('tuto/create/', views.JuegoInstanceCreate.as_view(), name='tuto_form'),
    path('tuto/<int:pk>/update/', views.JuegoInstanceUpdate.as_view(), name='tuto_update'),
    path('juego/<int:pk>/delete/', views.JuegoInstanceDelete.as_view(), name='tuto_delete'),

]