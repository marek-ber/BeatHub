from django.test import TestCase
from django.urls import reverse

from .models import Genre


class GenreModelTest(TestCase):

    def test_create_genre(self):
        genre = Genre.objects.create(
            name="Rock"
        )

        self.assertEqual(
            genre.name,
            "Rock"
        )


class ArtistListViewTest(TestCase):

    def test_artist_list_returns_200(self):
        response = self.client.get(
            reverse("artist_list")
        )

        self.assertEqual(
            response.status_code,
            200
        )