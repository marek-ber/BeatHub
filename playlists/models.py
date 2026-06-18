from django.db import models
from django.conf import settings

from music.models import Song


class Playlist(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
            related_name="playlists")
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    songs = models.ManyToManyField(Song, through="PlaylistSong")

    def __str__(self):
        return self.name


class PlaylistSong(models.Model):

    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.playlist.name} - {self.song.title}"