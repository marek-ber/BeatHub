from django.contrib import admin

from .models import Playlist, PlaylistSong


class PlaylistSongInline(admin.TabularInline):
    model = PlaylistSong
    extra = 1


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "owner", "songs_count"]
    search_fields = ["name", "owner__username"]
    list_filter = ["owner"]
    inlines = [PlaylistSongInline]

    def songs_count(self, obj):
        return obj.songs.count()

    songs_count.short_description = "Liczba utworów"


@admin.register(PlaylistSong)
class PlaylistSongAdmin(admin.ModelAdmin):
    list_display = ["id", "playlist", "song", "order"]
    search_fields = ["playlist__name", "song__title"]
    list_filter = ["playlist"]