from django.contrib import admin

from .models import Genre, Artist, Album, Song


class AlbumInline(admin.TabularInline):
    model = Album
    extra = 1


class SongInline(admin.TabularInline):
    model = Song
    extra = 1


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ["id", "pseudonym", "genres_list"]
    search_fields = ["pseudonym"]
    list_filter = ["genres"]
    inlines = [AlbumInline]

    def genres_list(self, obj):
        return ", ".join(genre.name for genre in obj.genres.all())

    genres_list.short_description = "Gatunki"


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "artist", "release_date"]
    search_fields = ["title", "artist__pseudonym"]
    list_filter = ["release_date", "artist"]
    inlines = [SongInline]


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "album", "artist_name", "duration_s"]
    search_fields = ["title", "album__title", "album__artist__pseudonym"]
    list_filter = ["album", "album__artist"]

    def artist_name(self, obj):
        return obj.album.artist.pseudonym

    artist_name.short_description = "Artysta"