from django.db import models
from django.urls import reverse

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    director = models.CharField(max_length=255)
    release_year = models.IntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    runtime = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    genre = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'pk': self.pk})
