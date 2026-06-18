from django.db import models


class Genre(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Artist(models.Model):

    pseudonym = models.CharField(max_length=250)
    image = models.ImageField(upload_to="artists/")
    genres = models.ManyToManyField(Genre, related_name="artists")

    def __str__(self):
        return self.pseudonym

class Album(models.Model):

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    title = models.CharField(max_length=250)
    release_date = models.DateField()
    cover = models.ImageField(upload_to="albums/")

    def __str__(self):
        return self.title

class Song(models.Model):

    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    title = models.CharField(max_length=250)
    duration_s = models.PositiveIntegerField()

    def duration_formatted(self):

        minutes = self.duration_s // 60

        seconds = self.duration_s % 60

        return f"{minutes}:{seconds:02d}"

    def __str__(self):
        return f"{self.album.artist.pseudonym} - {self.album.title} - {self.title}"