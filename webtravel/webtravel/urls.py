from django.contrib import admin
from django.urls import path
from applitravel import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('voyage/<int:voyage_id>/addvoyage/', views.ajouterEtape, name='etape-add'),
    path('voyages/<int:voyage_id>/delete/', views.supprimerVoyage, name='voyage-delete'),
    path('voyages/<int:voyage_id>/update/', views.afficherFormulaireModificationVoyage, name='voyage-update'),
    path('voyages/<int:voyage_id>/updated/', views.modifierVoyage, name='voyage-updated'),
    path('villes/<int:ville_id>/delete/', views.supprimerVille, name='ville-delete'),
    path('villes/<int:ville_id>/update/', views.afficherFormulaireModificationVille, name='ville-update'),
    path('villes/<int:ville_id>/updated/', views.modifierVille, name='ville-updated'),
    path('voyages/<int:voyage_id>/deleteEtape/<int:etape_id>/', views.supprimerEtapeDansVoyage, name='etape-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)