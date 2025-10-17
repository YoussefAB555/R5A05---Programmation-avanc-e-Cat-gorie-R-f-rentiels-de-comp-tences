from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.connexion, name='login'),
    path('logout/', views.deconnexion, name='logout'),
    path('user/update/', views.formulaireProfil, name='profil'),
    path('user/updated/', views.traitementFormulaireProfil, name='profil-update'),
]