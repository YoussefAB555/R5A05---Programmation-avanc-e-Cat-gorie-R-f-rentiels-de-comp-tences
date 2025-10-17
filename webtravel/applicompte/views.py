from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import TravelUser
from django.contrib.auth.decorators import login_required
from .forms import TravelUserForm, TravelUserImageForm

@login_required
def formulaireProfil(request):
    travel_user, created = TravelUser.objects.get_or_create(user=request.user)
    user_form = TravelUserForm(instance=request.user)
    image_form = TravelUserImageForm(instance=travel_user)
    return render(request, 'applicompte/profil.html', {'user_form': user_form, 'image_form': image_form, 'travel_user': travel_user})

@login_required
def traitementFormulaireProfil(request):
    travel_user, created = TravelUser.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        if 'update_profile' in request.POST:
            user_form = TravelUserForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                return redirect('profil')
        elif 'update_image' in request.POST:
            image_form = TravelUserImageForm(request.POST, request.FILES, instance=travel_user)
            if image_form.is_valid():
                image_form.save()
                return redirect('profil')
    return redirect('profil')

def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'applicompte/login.html', {'form': form})

def deconnexion(request):
    logout(request)
    return render(request, 'applicompte/logout.html')