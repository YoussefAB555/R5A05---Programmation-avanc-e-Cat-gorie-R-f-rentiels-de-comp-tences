from django.shortcuts import render, get_object_or_404, redirect
from .models import Voyage, Ville, Composition, Commande, LigneCommande
from .forms import VilleForm, VoyageForm
from django.contrib.auth.models import User
from applicompte.models import TravelUser
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.db.models import Sum, Count

def home(request):
    travel_user = None
    if request.user.is_authenticated:
        travel_user, created = TravelUser.objects.get_or_create(user=request.user)
    return render(request, 'applitravel/home.html', {'travel_user': travel_user})

def voyages(request):
    travel_user = None
    if request.user.is_authenticated:
        travel_user, created = TravelUser.objects.get_or_create(user=request.user)
    return render(request, 'applitravel/voyages.html',
                  {'voyages': Voyage.objects.all(), 'travel_user': travel_user})

from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(lambda u: u.is_staff)
def villes(request):
    travel_user = None
    if request.user.is_authenticated:
        travel_user, created = TravelUser.objects.get_or_create(user=request.user)
    return render(request, 'applitravel/villes.html',
                  {'villes': Ville.objects.all(), 'travel_user': travel_user})

def voyage(request, voyage_id:int):
    v = get_object_or_404(Voyage, IDVoyage=voyage_id)
    etapes = Composition.objects.filter(voyage=v)
    villes = Ville.objects.all()
    travel_user = None
    if request.user.is_authenticated:
        travel_user, created = TravelUser.objects.get_or_create(user=request.user)
    return render(request, 'applitravel/voyage.html', {'voyage': v, 'etapes': etapes, 'lesVilles': villes, 'travel_user': travel_user})

@login_required
@user_passes_test(lambda u: u.is_staff)
def formulaireCreationVille(request):
    return render(request, 'applitravel/formulaireCreationVille.html', {'form': VilleForm()})

@login_required
@user_passes_test(lambda u: u.is_staff)
def creerVille(request):
    if request.method == 'POST':
        form = VilleForm(request.POST)
        if form.is_valid():
            ville = form.save()
            return render(request, 'applitravel/traitementFormulaireCreationVille.html', {'nom': ville.NomVille})
    return redirect('ville-add')

@login_required
@user_passes_test(lambda u: u.is_staff)
def formulaireCreationVoyage(request):
    return render(request, 'applitravel/formulaireCreationVoyage.html', {'form': VoyageForm()})

@login_required
@user_passes_test(lambda u: u.is_staff)
def creerVoyage(request):
    if request.method == 'POST':
        form = VoyageForm(request.POST, request.FILES)
        if form.is_valid():
            v = form.save()
            return render(request, 'applitravel/traitementFormulaireCreationVoyage.html', {'titre': v.Titre})
    return redirect('voyage-add')

@login_required
@user_passes_test(lambda u: u.is_staff)
def ajouterEtape(request, voyage_id):
    voyage = get_object_or_404(Voyage, IDVoyage=voyage_id)
    if request.method == 'POST':
        ville_id = request.POST.get('ville')
        nb_jours = request.POST.get('Nb_Jours')
        ville = get_object_or_404(Ville, IDVille=ville_id)
        
        # Si l'étape existe déjà, on la supprime avant de la recréer
        Composition.objects.filter(voyage=voyage, ville=ville).delete()
        
        etape = Composition(voyage=voyage, ville=ville, nbJours=nb_jours)
        etape.save()
        
    return redirect('voyage-detail', voyage_id=voyage.IDVoyage)

@login_required
@user_passes_test(lambda u: u.is_staff)
def supprimerVoyage(request, voyage_id):
    voyage = get_object_or_404(Voyage, IDVoyage=voyage_id)
    voyage.delete()
    return redirect('voyages')

@login_required
@user_passes_test(lambda u: u.is_staff)
def supprimerVille(request, ville_id):
    ville = get_object_or_404(Ville, IDVille=ville_id)
    ville.delete()
    return redirect('villes')

@login_required
@user_passes_test(lambda u: u.is_staff)
def afficherFormulaireModificationVoyage(request, voyage_id):
    voyage = get_object_or_404(Voyage, IDVoyage=voyage_id)
    form = VoyageForm(instance=voyage)
    return render(request, 'applitravel/formulaireModificationVoyage.html', {'form': form, 'voyage_id': voyage_id})

@login_required
@user_passes_test(lambda u: u.is_staff)
def modifierVoyage(request, voyage_id):
    voyage = get_object_or_404(Voyage, IDVoyage=voyage_id)
    if request.method == 'POST':
        form = VoyageForm(request.POST, request.FILES, instance=voyage)
        if form.is_valid():
            form.save()
            return redirect('voyage-detail', voyage_id=voyage_id)
    return redirect('voyage-update', voyage_id=voyage_id)

@login_required
@user_passes_test(lambda u: u.is_staff)
def afficherFormulaireModificationVille(request, ville_id):
    ville = get_object_or_404(Ville, IDVille=ville_id)
    form = VilleForm(instance=ville)
    return render(request, 'applitravel/formulaireModificationVille.html', {'form': form, 'ville_id': ville_id})

@login_required
@user_passes_test(lambda u: u.is_staff)
def modifierVille(request, ville_id):
    ville = get_object_or_404(Ville, IDVille=ville_id)
    if request.method == 'POST':
        form = VilleForm(request.POST, instance=ville)
        if form.is_valid():
            form.save()
            return redirect('villes')
    return redirect('ville-update', ville_id=ville_id)

@login_required
@user_passes_test(lambda u: u.is_staff)
def supprimerEtapeDansVoyage(request, voyage_id, etape_id):
    etape = get_object_or_404(Composition, IDEtape=etape_id)
    etape.delete()
    return redirect('voyage-detail', voyage_id=voyage_id)

@login_required
def afficherPanier(request):
    commande, created = Commande.objects.get_or_create(user=request.user, payee=False)
    return render(request, 'applitravel/panier.html', {'commande': commande})

@login_required
def ajouterVoyageAuPanier(request, voyage_id):
    voyage = get_object_or_404(Voyage, IDVoyage=voyage_id)
    commande, created = Commande.objects.get_or_create(user=request.user, payee=False)
    ligne, created = LigneCommande.objects.get_or_create(commande=commande, voyage=voyage)
    if not created:
        ligne.quantite += 1
        ligne.save()
    return redirect('panier')

@login_required
def retirerUnVoyageDuPanier(request, voyage_id):
    voyage = get_object_or_404(Voyage, IDVoyage=voyage_id)
    commande = get_object_or_404(Commande, user=request.user, payee=False)
    ligne = get_object_or_404(LigneCommande, commande=commande, voyage=voyage)
    if ligne.quantite > 1:
        ligne.quantite -= 1
        ligne.save()
    else:
        ligne.delete()
    return redirect('panier')

@login_required
def retirerDuPanier(request, voyage_id):
    voyage = get_object_or_404(Voyage, IDVoyage=voyage_id)
    commande = get_object_or_404(Commande, user=request.user, payee=False)
    ligne = get_object_or_404(LigneCommande, commande=commande, voyage=voyage)
    ligne.delete()
    return redirect('panier')

@login_required
def viderPanier(request):
    commande = get_object_or_404(Commande, user=request.user, payee=False)
    commande.delete()
    return redirect('panier')

@login_required
def payerPanier(request):
    commande = get_object_or_404(Commande, user=request.user, payee=False)
    commande.payee = True
    commande.save()
    return render(request, 'applitravel/avisPaiement.html', {'commande': commande})

@login_required
@user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    return render(request, 'applitravel/dashboard.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
def clients(request):
    clients = User.objects.filter(is_staff=False)
    return render(request, 'applitravel/clients.html', {'clients': clients})

@login_required
@user_passes_test(lambda u: u.is_staff)
def historiqueToutesCommandes(request):
    commandes = Commande.objects.filter(payee=True).order_by('-date_commande')
    return render(request, 'applitravel/historiqueToutesCommandes.html', {'commandes': commandes})

@login_required
@user_passes_test(lambda u: u.is_staff)
def revenus(request):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    
    commandes = Commande.objects.filter(payee=True, date_commande__range=[start_date, end_date])
    
    daily_revenue = {}
    for i in range(8):
        date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
        daily_revenue[date] = 0

    for commande in commandes:
        date_str = commande.date_commande.strftime('%Y-%m-%d')
        daily_revenue[date_str] += commande.total

    labels = list(daily_revenue.keys())
    data = list(daily_revenue.values())
    
    return JsonResponse({'labels': labels, 'data': data})

@login_required
@user_passes_test(lambda u: u.is_staff)
def revenus_page(request):
    return render(request, 'applitravel/revenus.html')

@login_required
@user_passes_test(lambda u: u.is_staff)
def ventes(request):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    
    lignes = LigneCommande.objects.filter(commande__payee=True, commande__date_commande__range=[start_date, end_date])
    sales_data = lignes.values('voyage__Titre').annotate(total_sales=Sum('quantite')).order_by('-total_sales')
    
    labels = [item['voyage__Titre'] for item in sales_data]
    data = [item['total_sales'] for item in sales_data]
    
    return JsonResponse({'labels': labels, 'data': data})

@login_required
@user_passes_test(lambda u: u.is_staff)
def ventes_page(request):
    return render(request, 'applitravel/ventes.html')
