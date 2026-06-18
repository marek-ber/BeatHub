import random

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from faker import Faker

from music.models import Genre, Artist, Album, Song
from playlists.models import Playlist, PlaylistSong


class Command(BaseCommand):
    help = "Generuje dane testowe dla BeatHub"

    def handle(self, *args, **kwargs):
        fake = Faker("pl_PL")
        User = get_user_model()

        genres = []
        genre_names = [
            "Hip-Hop",
            "Rock",
            "Pop",
            "Metal",
            "Electronic",
            "Jazz",
        ]

        for name in genre_names:
            genre, created = Genre.objects.get_or_create(name=name)
            genres.append(genre)

        users = []

        for i in range(5):
            username = f"user{i + 1}"

            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    "email": f"user{i + 1}@example.com"
                }
            )

            if created:
                user.set_password("test12345")
                user.save()

            users.append(user)

        artists = []

        for _ in range(10):
            artist = Artist.objects.create(
                pseudonym=fake.name(),
                image="artists/default.jpg"
            )

            artist.genres.set(
                random.sample(genres, k=random.randint(1, 2))
            )

            artists.append(artist)

        albums = []

        for artist in artists:
            for _ in range(random.randint(1, 3)):
                album = Album.objects.create(
                    artist=artist,
                    title=fake.sentence(nb_words=3),
                    release_date=fake.date_between(
                        start_date="-20y",
                        end_date="today"
                    ),
                    cover="albums/default.jpg"
                )

                albums.append(album)

                for _ in range(random.randint(5, 10)):
                    Song.objects.create(
                        album=album,
                        title=fake.sentence(nb_words=3),
                        duration_s=random.randint(120, 420)
                    )

        songs = list(Song.objects.all())

        for user in users:
            for _ in range(2):
                playlist = Playlist.objects.create(
                    owner=user,
                    name=fake.sentence(nb_words=2),
                    description=fake.text(max_nb_chars=120)
                )

                selected_songs = random.sample(
                    songs,
                    k=min(5, len(songs))
                )

                for index, song in enumerate(selected_songs, start=1):
                    PlaylistSong.objects.create(
                        playlist=playlist,
                        song=song,
                        order=index
                    )

        self.stdout.write(
            self.style.SUCCESS("Dane testowe zostały wygenerowane.")
        )