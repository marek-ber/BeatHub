from django import forms
from .models import Playlist
from music.models import Song


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ["name", "description"]


class AddSongToPlaylistForm(forms.Form):
    song = forms.ModelChoiceField(
        queryset=Song.objects.all(),
        label="Piosenka"
    )