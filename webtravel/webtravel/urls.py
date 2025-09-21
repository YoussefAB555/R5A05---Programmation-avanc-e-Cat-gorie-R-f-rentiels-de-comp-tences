from django.contrib import admin
from django.urls import path
from applitravel import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('voyages/', views.voyages, name='voyages'),
    path('villes/', views.villes, name='villes'),
    path('voyages/<int:voyage_id>/', views.voyage, name='voyage-detail'),
    path('villes/add', views.formulaireCreationVille, name='ville-add'),
    path('villes/create', views.creerVille, name='ville-create'),
    path('voyages/add', views.formulaireCreationVoyage, name='voyage-add'),
    path('voyages/create', views.creerVoyage, name='voyage-create'),
]