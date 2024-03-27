from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MovieForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

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

class MovieCreateView(CreateView):
    model = Movie
    fields = ['title', 'description', 'director', 'release_year', 'budget', 'runtime', 'rating', 'genre']
    success_url = reverse_lazy('movie-list')

class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_update_form.html'

class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie-list')
    template_name = 'movies/movie_confirm_delete.html'
