from django.core.handlers import exception
from django.shortcuts import render, redirect

from GamesPlayApp.gamesplay.forms import CreateProfileForm
from GamesPlayApp.gamesplay.models import Profile


# Create your views here.


def index(request):
    profile = Profile.objects.all().first()
    context = {
         'profile': profile,
    }
    return render(request, 'core/home-page.html', context)


def create_profile(request):
    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context)


def dashboard(request):
    pass


def create_game(request):
    pass


def details_game(request, pk):
    pass


def edit_game(request, pk):
    pass


def delete_game(request, pk):
    pass


def details_profile(request):
    pass


def edit_profile(request):
    pass


def delete_profile(request):
    pass