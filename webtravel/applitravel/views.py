from django.shortcuts import render, get_object_or_404, redirect
from .models import Voyage, Ville, Composition
from .forms import VilleForm, VoyageForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

def home(request): return render(request, 'applitravel/home.html')

def voyages(request):
    return render(request, 'applitravel/voyages.html',
                  {'voyages': Voyage.objects.all()})

from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(lambda u: u.is_staff)
def villes(request):
    return render(request, 'applitravel/villes.html',
                  {'villes': Ville.objects.all()})

def voyage(request, voyage_id:int):
    v = get_object_or_404(Voyage, IDVoyage=voyage_id)
    etapes = Composition.objects.filter(voyage=v)
    villes = Ville.objects.all()
    return render(request, 'applitravel/voyage.html', {'voyage': v, 'etapes': etapes, 'lesVilles': villes})

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



