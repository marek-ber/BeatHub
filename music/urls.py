from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("artists/", views.artist_list, name="artist_list"),
    path("artists/<int:artist_id>/", views.artist_detail, name="artist_detail"),
    path("albums/<int:album_id>/", views.album_detail, name="album_detail"),
    path("search/", views.search_view, name="search"),
]