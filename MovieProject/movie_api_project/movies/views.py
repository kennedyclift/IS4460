from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from django.shortcuts import render, redirect
from .forms import MovieForm

class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie-list')
    else:
        form = MovieForm()
    return render(request, 'movie_add.html', {'form': form})
