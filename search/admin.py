from django.contrib import admin
from .models import Movie

class DoubanAdmin(admin.ModelAdmin):
    list_display = ('movie_id', 'movie', 'other_name', 'director', 'actor', 'year', 'rate', 'first_introduction',)

admin.site.register(Movie, DoubanAdmin)


# Register your models here.
