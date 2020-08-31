from django.shortcuts import render, redirect
from.models import Game
from .forms import GameForm

def profile(request):
    return render(request, 'crud.html')


def profile(request):
    games = Game.objects.all()
    return render(request, 'profile.html', {'games': games})


def register_game(request):
    form = GameForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'game-form.html', {'form': form})


def update_game(request, id):
    games = Game.objects.get(id=id)
    form = GameForm(request.POST or None, instance=games)

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'game-form.html', {'form': form, 'games': games})


def delete_game(request, id):
    games = Game.objects.get(id=id)

    if request.method == 'POST':
        games.delete()
        return redirect('profile')

    return render(request, 'game-delete-ok.html', {'games': games})
