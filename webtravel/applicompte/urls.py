from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.formulaireInscription, name='register'),
    path('register/submit/', views.traitementFormulaireInscription, name='traitement_register'),
    path('login/', views.connexion, name='login'),
    path('logout/', views.deconnexion, name='logout'),
    path('profil/', views.formulaireProfil, name='profil'),
    path('profil/submit/', views.traitementFormulaireProfil, name='traitement_profil'),
]
