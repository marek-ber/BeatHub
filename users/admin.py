from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "bio_short"]
    search_fields = ["user__username", "bio"]

    def bio_short(self, obj):
        return obj.bio[:50]

    bio_short.short_description = "Bio"