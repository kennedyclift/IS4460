from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MovieForm


class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie-list.html', {'movies': movies})

def movie_details(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie-details.html', {'movie': movie})

def movie_add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie-list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie-add.html', {'form': form})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie-list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie-update.html', {'form': form, 'movie': movie})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie-list')
    return render(request, 'movies/movie-delete.html', {'movie': movie})
