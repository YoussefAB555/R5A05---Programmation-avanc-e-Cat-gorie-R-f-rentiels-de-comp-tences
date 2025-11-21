from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.formulaireInscription, name='register'),
    path('register/submit/', views.traitementFormulaireInscription, name='traitement_register'),
    path('login/', views.connexion, name='login'),
    path('logout/', views.deconnexion, name='logout'),
    path('profil/', views.formulaireProfil, name='profil'),
    path('profil/submit/', views.traitementFormulaireProfil, name='traitement_profil'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='applicompte/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='applicompte/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='applicompte/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='applicompte/password_reset_complete.html'), name='password_reset_complete'),
]
