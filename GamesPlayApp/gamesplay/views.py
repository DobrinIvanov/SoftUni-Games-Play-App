# from django.core.handlers import exception
from django.shortcuts import render, redirect

from GamesPlayApp.gamesplay.forms import CreateProfileForm, CreateGameForm, EditGameForm
from GamesPlayApp.gamesplay.models import Profile, Game


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
    games = Game.objects.all()

    context = {
        'games': games,

    }
    return render(request, 'core/dashboard.html', context)


def create_game(request):
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
    }
    return render(request, 'games/create-game.html', context)


def details_game(request, pk):
    game = Game.objects.filter(pk=pk).first()
    context = {
        'game': game,
    }
    return render(request, 'games/details-game.html', context)


def edit_game(request, pk):
    instance = Game.objects.filter(pk=pk).first()
    if request.method == 'GET':
        form = EditGameForm(instance=instance)
    else:
        form = EditGameForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'game': instance,
    }
    return render(request, 'games/edit-game.html', context)


def delete_game(request, pk):
    pass


def details_profile(request):
    pass


def edit_profile(request):
    pass


def delete_profile(request):
    pass