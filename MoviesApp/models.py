from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    imdbID = models.CharField(null = True, max_length = 20)
    title = models.CharField(max_length = 100)
    year = models.IntegerField()
    director = models.CharField(blank = True, null = True, max_length = 40)
    plot = models.TextField(blank = True, null = True)
    imdbRating = models.CharField(blank = True, null = True, max_length = 20)
    moviePic = models.ImageField(upload_to = 'movie_pics', default = 'default.jpeg')

    def get_absolute_url(self):
        return reverse('userdetail', kwargs={'pk': self.pk })

class Critic(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    criticText = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
