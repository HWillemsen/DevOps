from django.contrib import admin

from .models import Movie, Critic

# Register your models here.
admin.site.register(Movie)
admin.site.register(Critic)
