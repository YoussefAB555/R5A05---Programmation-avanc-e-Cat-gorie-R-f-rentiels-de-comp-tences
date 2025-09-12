from django.shortcuts import render, get_object_or_404, redirect
from .models import Voyage, Ville, Composition
from .forms import VilleForm, VoyageForm

def home(request): return render(request, 'applitravel/home.html')

def voyages(request):
    return render(request, 'applitravel/voyages.html',
                  {'voyages': Voyage.objects.all()})

def villes(request):
    return render(request, 'applitravel/villes.html',
                  {'villes': Ville.objects.all()})

def voyage(request, voyage_id:int):
    v = get_object_or_404(Voyage, IDVoyage=voyage_id)
    etapes = Composition.objects.filter(voyage=v)
    villes = Ville.objects.all()
    return render(request, 'applitravel/voyage.html', {'voyage': v, 'etapes': etapes, 'lesVilles': villes})

def formulaireCreationVille(request):
    return render(request, 'applitravel/formulaireCreationVille.html', {'form': VilleForm()})

def creerVille(request):
    if request.method == 'POST':
        form = VilleForm(request.POST)
        if form.is_valid():
            ville = form.save()
            return render(request, 'applitravel/traitementFormulaireCreationVille.html', {'nom': ville.NomVille})
    return redirect('ville-add')

def formulaireCreationVoyage(request):
    return render(request, 'applitravel/formulaireCreationVoyage.html', {'form': VoyageForm()})

def creerVoyage(request):
    if request.method == 'POST':
        form = VoyageForm(request.POST)
        if form.is_valid():
            v = form.save()
            return render(request, 'applitravel/traitementFormulaireCreationVoyage.html', {'titre': v.Titre})
    return redirect('voyage-add')

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



