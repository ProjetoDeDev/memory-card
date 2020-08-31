from django import forms
from .models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name_game', 'author', 'release_year', 'text', 'date_publish', 'game_img']
