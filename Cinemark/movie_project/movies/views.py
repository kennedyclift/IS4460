from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MovieForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy

class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCreateView(CreateView):
    model = Movie
    fields = ['title', 'description', 'director', 'release_year', 'budget', 'runtime', 'rating', 'genre']
    success_url = reverse_lazy('movie-list')

class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movie_list'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_update_form.html'


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie-list')
    template_name = 'movies/movie_confirm_delete.html'

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movie_list': movies})

def movie_details(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_details.html', {'movie': movie})

def movie_add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie-list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_add.html', {'form': form}) 
