from django.db import models
from actors.models import Actor
from genres.models import Genre

class Movie(models.Model):
    title = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="movies") # vai proteger de exclusao 
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name="movies") # relaça de N: -> N: 
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

        # 5.51