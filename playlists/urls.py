from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.playlist_create, name="playlist_create"),
    path("<int:playlist_id>/", views.playlist_detail, name="playlist_detail"),
    path("<int:playlist_id>/add-song/", views.add_song_to_playlist, name="add_song_to_playlist"),
    path("song/<int:playlist_song_id>/remove/", views.remove_song_from_playlist, name="remove_song_from_playlist"),
    path("<int:playlist_id>/edit/", views.playlist_update, name="playlist_update"),
    path("<int:playlist_id>/delete/", views.playlist_delete, name="playlist_delete"),
    path("song/<int:playlist_song_id>/up/", views.move_song_up, name="move_song_up"),
    path("song/<int:playlist_song_id>/down/", views.move_song_down, name="move_song_down"),
]