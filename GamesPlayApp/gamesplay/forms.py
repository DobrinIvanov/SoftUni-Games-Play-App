from django import forms

from GamesPlayApp.gamesplay.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class CreateGameForm(GameForm):
    pass


class EditGameForm(GameForm):
    pass
