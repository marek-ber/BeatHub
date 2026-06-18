from django.shortcuts import render, get_object_or_404
from .models import Artist, Album, Song, Genre


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, "music/artist_list.html", {"artists": artists})


def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    albums = artist.albums.all()
    return render(request, "music/artist_detail.html", {
        "artist": artist,
        "albums": albums,
    })


def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    songs = album.songs.all()
    return render(request, "music/album_detail.html", {
        "album": album,
        "songs": songs,
    })

def home_view(request):
    artists = Artist.objects.all()[:6]
    albums = Album.objects.all()[:6]
    songs = Song.objects.all()[:5]

    return render(
        request,
        "music/home.html",
        {
            "artists": artists,
            "albums": albums,
            "songs": songs,
        }
    )

def search_view(request):
    query = request.GET.get("q", "")

    artists = Artist.objects.none()
    albums = Album.objects.none()
    songs = Song.objects.none()
    genres = Genre.objects.none()

    if query:
        artists = Artist.objects.filter(
            pseudonym__icontains=query
        ) | Artist.objects.filter(
            genres__name__icontains=query
        )

        albums = Album.objects.filter(
            title__icontains=query
        ) | Album.objects.filter(
            artist__pseudonym__icontains=query
        ) | Album.objects.filter(
            artist__genres__name__icontains=query
        )

        songs = Song.objects.filter(
            title__icontains=query
        ) | Song.objects.filter(
            album__title__icontains=query
        ) | Song.objects.filter(
            album__artist__pseudonym__icontains=query
        ) | Song.objects.filter(
            album__artist__genres__name__icontains=query
        )

        genres = Genre.objects.filter(
            name__icontains=query
        )

    return render(request, "music/search.html", {
        "query": query,
        "artists": artists.distinct(),
        "albums": albums.distinct(),
        "songs": songs.distinct(),
        "genres": genres,
    })