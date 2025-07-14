from django.contrib import admin
from .models import Album, Artist, UserFavorite, Track

admin.site.register(Artist)
admin.site.register(UserFavorite)

class TrackInline(admin.TabularInline):
    model = Track
    extra = 1 

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [TrackInline]

admin.site.register(Track)
