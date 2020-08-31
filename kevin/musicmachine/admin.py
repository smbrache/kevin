from django.contrib import admin
from .models import Song


# Define and register the admin class for Song
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'tempo', 'summary')
    fields = ['title', 'creator', 'tempo', 'summary']
    list_filter = ('title', 'creator', 'tempo')
