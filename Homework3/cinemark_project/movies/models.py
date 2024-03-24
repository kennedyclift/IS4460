from django.db import models

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    director = models.CharField(max_length=255)
    release_year = models.IntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    runtime = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.title
