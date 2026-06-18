from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import PlaylistForm, AddSongToPlaylistForm
from .models import Playlist, PlaylistSong


@login_required
def playlist_create(request):
    if request.method == "POST":
        form = PlaylistForm(request.POST)

        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.owner = request.user
            playlist.save()

            return redirect("playlist_detail", playlist.id)

    else:
        form = PlaylistForm()

    return render(request, "playlists/playlist_form.html", {"form": form})


def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(
        Playlist,
        id=playlist_id
    )

    playlist_songs = (
        playlist.playlistsong_set
        .all()
        .order_by("order")
    )

    return render(
        request,
        "playlists/playlist_detail.html",
        {
            "playlist": playlist,
            "playlist_songs": playlist_songs,
        }
    )

@login_required
def add_song_to_playlist(request, playlist_id):
    playlist = get_object_or_404(
        Playlist,
        id=playlist_id,
        owner=request.user
    )

    if request.method == "POST":
        form = AddSongToPlaylistForm(request.POST)

        if form.is_valid():
            song = form.cleaned_data["song"]

            last_song = PlaylistSong.objects.filter(
                playlist=playlist
            ).order_by("-order").first()

            if last_song:
                next_order = last_song.order + 1
            else:
                next_order = 1

            PlaylistSong.objects.create(
                playlist=playlist,
                song=song,
                order=next_order
            )

            return redirect("playlist_detail", playlist.id)

    else:
        form = AddSongToPlaylistForm()

    return render(
        request,
        "playlists/add_song.html",
        {
            "form": form,
            "playlist": playlist
        }
    )

@login_required
def remove_song_from_playlist(request, playlist_song_id):
    playlist_song = get_object_or_404(
        PlaylistSong,
        id=playlist_song_id,
        playlist__owner=request.user
    )

    playlist_id = playlist_song.playlist.id

    playlist_song.delete()

    return redirect("playlist_detail", playlist_id)


@login_required
def playlist_update(request, playlist_id):
    playlist = get_object_or_404(
        Playlist,
        id=playlist_id,
        owner=request.user
    )

    if request.method == "POST":
        form = PlaylistForm(request.POST, instance=playlist)

        if form.is_valid():
            form.save()
            return redirect("playlist_detail", playlist.id)

    else:
        form = PlaylistForm(instance=playlist)

    return render(
        request,
        "playlists/playlist_form.html",
        {"form": form}
    )


@login_required
def playlist_delete(request, playlist_id):
    playlist = get_object_or_404(
        Playlist,
        id=playlist_id,
        owner=request.user
    )

    if request.method == "POST":
        playlist.delete()
        return redirect("profile",
            username=request.user.username)

    return render(
        request,
        "playlists/playlist_confirm_delete.html",
        {"playlist": playlist}
    )



@login_required
def move_song_up(request, playlist_song_id):

    playlist_song = get_object_or_404(
        PlaylistSong,
        id=playlist_song_id,
        playlist__owner=request.user
    )

    previous_song = (
        PlaylistSong.objects
        .filter(
            playlist=playlist_song.playlist,
            order__lt=playlist_song.order
        )
        .order_by("-order")
        .first()
    )

    if previous_song:

        playlist_song.order, previous_song.order = (
            previous_song.order,
            playlist_song.order
        )

        playlist_song.save()
        previous_song.save()

    return redirect(
        "playlist_detail",
        playlist_song.playlist.id
    )

@login_required
def move_song_down(request, playlist_song_id):

    playlist_song = get_object_or_404(
        PlaylistSong,
        id=playlist_song_id,
        playlist__owner=request.user
    )

    next_song = (
        PlaylistSong.objects
        .filter(
            playlist=playlist_song.playlist,
            order__gt=playlist_song.order
        )
        .order_by("order")
        .first()
    )

    if next_song:

        playlist_song.order, next_song.order = (
            next_song.order,
            playlist_song.order
        )

        playlist_song.save()
        next_song.save()

    return redirect(
        "playlist_detail",
        playlist_song.playlist.id
    )