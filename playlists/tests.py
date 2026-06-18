from django.test import TestCase
from django.urls import reverse


class PlaylistPermissionTest(TestCase):

    def test_playlist_create_requires_login(self):

        response = self.client.get(
            reverse("playlist_create")
        )

        self.assertEqual(
            response.status_code,
            302
        )