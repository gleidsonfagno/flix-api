from django.contrib import admin
from movies.models import Movie


@admin.register(Movie) # para registrar no admin
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "genre", "release_date", "resume",)
